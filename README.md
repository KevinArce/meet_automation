# Automated Google Meet Link Opener

This Python script allows you to automatically open a Google Meet link at a specified time and on specific days of the week using the `schedule` library.

## Prerequisites

Before you can run this script, make sure you have set up a virtual environment and installed the `schedule` library. You can do this by following these steps:

1. Create a virtual environment:

2. Activate the virtual environment (on Windows):

3. Install the `schedule` library:

## Usage

1. Clone this repository to your local machine or download the script.

2. Edit the script to replace `'YOUR GOOGLE MEET LINK'` with the actual Google Meet meeting URL you want to open.

3. Customize the scheduling by modifying the `schedule.every()` lines. By default, the script is set to open the Google Meet link every Tuesday to Friday at 8 AM. You can adjust the days and time to meet your specific needs.

4. Run the script:

python meeting_scheduler.py

The script will run in the background and automatically open the Google Meet link at the scheduled times.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
