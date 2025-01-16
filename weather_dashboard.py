import os
import json
import boto3
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class WeatherDashboard:
    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.bucket_name = os.getenv('S3_BUCKET_NAME')
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
            aws_secret_access_key=os.getenv('AWS_SECRET_KEY'),
            region_name=os.getenv('AWS_REGION')
        )

        if not self.api_key:
            raise ValueError("OPENWEATHER_API_KEY is not set")
        if not self.bucket_name:
            raise ValueError("S3_BUCKET_NAME is not set")
        if not os.getenv('AWS_ACCESS_KEY') or not os.getenv('AWS_SECRET_KEY'):
            raise ValueError("AWS credentials are not set")
        if not os.getenv('AWS_REGION'):
            raise ValueError("AWS_REGION is not set")
        
    def create_bucket_if_not_exists(self):
        """Create S3 bucket if it doesn't exist"""
        try:
            self.s3_client.head_bucket(Bucket=self.bucket_name)
            print(f"Bucket {self.bucket_name} exists")
        except self.s3_client.exceptions.NoSuchBucket:
            try:
                self.s3_client.create_bucket(Bucket=self.bucket_name)
                print(f"Bucket {self.bucket_name} created")
            except Exception as e:
                print(f"Error creating bucket: {e}")

    def fetch_weather(self, city):
        """Fetch weather data for a given city"""
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={self.api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            weather_data = response.json()
            self.display_weather_data(city, weather_data)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            print(f"Failed to fetch weather data for {city}")

    def display_weather_data(self, city, weather_data):
        """Display weather data in a readable format"""
        print(f"Weather data for {city}:")
        print(f"Temperature: {weather_data['main']['temp']}°F")
        print(f"Weather: {weather_data['weather'][0]['description']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} mph")
        print(f"Timestamp: {datetime.fromtimestamp(weather_data['dt'])}")
        print("-" * 40)

    def save_weather_data_to_s3(self, city, weather_data):
        """Save weather data to S3"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"{city}_{timestamp}.json"
        try:
            weather_data['timestamp'] = timestamp
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=file_name,
                Body=json.dumps(weather_data),
                ContentType='application/json'
            )
            print(f"Successfully saved data for {city} to S3")
            return True
        except Exception as e:
            print(f"Error saving to S3: {e}")
            return False

def main():
    dashboard = WeatherDashboard()
    dashboard.create_bucket_if_not_exists()
    cities = ["Philadelphia", "Seattle", "New York"]
    for city in cities:
        dashboard.fetch_weather(city)

if __name__ == "__main__":
    main()