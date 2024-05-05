# ISS Tracker and Sky Notification System

This Python script tracks the International Space Station (ISS) and notifies the user via email if the ISS is overhead and the sky is dark enough for observation. It utilizes two APIs: one to track the current position of the ISS and another to determine sunrise and sunset times at the user's location.

## Getting Started

Before running the script, you'll need to provide some configuration details and dependencies.

### Dependencies

- `requests`: Install using `pip install requests`.
- `convert24.py`: A module that converts time from 12-hour format to 24-hour format. Ensure you have this file in the same directory as the script.

### Configuration

1. Update the following variables with your own values:
   - `HOST`: SMTP host for your email provider (e.g., "smtp.gmail.com").
   - `MY_EMAIL`: Your email address.
   - `PASSWORD`: Your email account password (you may need to generate an app password for this).
   - `MY_LAT` and `MY_LONG`: Your latitude and longitude coordinates. (you can find your coordinates using this website: `https://www.latlong.net/`)

## Usage

1. Run the script:

   ```bash
   python iss_tracker.py
   ```

2. The script will check if the ISS is overhead and if the sky is dark enough for observation.
3. If both conditions are met, it will send an email notification to your specified email address.
4. Check your email inbox for the notification.

## Features

- Tracks the current position of the International Space Station (ISS).
- Determines if the ISS is overhead within a certain range of latitude and longitude.
- Determines if the sky is dark enough for observation based on sunrise and sunset times at the user's location.
- Sends an email notification if both conditions are met.

## Project Structure

- `iss_tracker.py`: Main Python script containing the implementation of the ISS tracker and sky notification system.
- `convert24.py`: Module for converting time from 12-hour format to 24-hour format. You can find it in the repository.
- `README.md`: Markdown file containing information about the script and how to use it.

## Contributing

Contributions are welcome! If you have any suggestions, enhancements, or bug fixes, feel free to open an issue or create a pull request.

## Contact

For any inquiries or support, please contact [abhijeetsapar17@gmail.com].
