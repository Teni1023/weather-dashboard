# Weather Dashboard

## Overview

The Weather Dashboard is a Python-based application that fetches weather data for specified cities and stores the data in an AWS S3 bucket. The application uses the OpenWeather API to retrieve weather information and the Boto3 library to interact with AWS S3.

## Features

- Fetches current weather data for specified cities.
- Displays weather data in a readable format.
- Stores weather data in an AWS S3 bucket.
- Handles errors gracefully and provides informative messages.

## Prerequisites

- Python 3.6 or higher
- An AWS account with S3 access
- OpenWeather API key

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Teni1023/weather-dashboard.git
    cd weather-dashboard
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your environment variables:

    ```plaintext
    OPENWEATHER_API_KEY=your_openweather_api_key
    AWS_ACCESS_KEY=your_aws_access_key
    AWS_SECRET_KEY=your_aws_secret_key
    AWS_REGION=your_aws_region
    S3_BUCKET_NAME=your_s3_bucket_name
    ```

## Usage

1. Run the application:

    ```bash
    python src/weather_dashboard.py
    ```

2. The application will fetch weather data for the specified cities and display it in a readable format. It will also save the weather data to the specified S3 bucket.

## Code Structure

- [weather_dashboard.py](http://_vscodecontentref_/0): The main script that contains the [WeatherDashboard](http://_vscodecontentref_/1) class and the logic for fetching and displaying weather data, as well as saving it to S3.

## Methods

### [__init__()](http://_vscodecontentref_/2)

Initializes the [WeatherDashboard](http://_vscodecontentref_/3) class and loads environment variables.

### `create_bucket_if_not_exists()`

Creates the S3 bucket if it doesn't exist.

### `fetch_weather(city)`

Fetches weather data for a given city.

### `display_weather_data(city, weather_data)`

Displays weather data in a readable format.

### `save_weather_data_to_s3(city, weather_data)`

Saves weather data to the specified S3 bucket.

## Example Output

```plaintext
Bucket my-weather-bucket exists
Fetching weather for Philadelphia...
Weather data for Philadelphia:
Temperature: 75°F
Weather: clear sky
Humidity: 50%
Wind Speed: 5 mph
Timestamp: 2023-10-01 12:00:00
----------------------------------------
Successfully saved data for Philadelphia to S3
