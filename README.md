# AutomatedFeedbackUploader

**README.md**

## Description

This Python script is designed to upload feedback stored in text files, all written in the same format (i.e., title, name, date, and feedback), to the company's website without having to turn it into a dictionary one by one.

## Instructions

Follow the steps below to use the script:

1. Place all the feedback text files in the `/data/feedback` directory.

2. Execute the Python script, and it will automatically upload the feedback to the company's website.

## Steps Performed by the Script

The script follows the structure below to upload the feedback:

1. Lists all `.txt` files under the `/data/feedback` directory that contains the actual feedback to be displayed on the company's website. It uses the `os.listdir()` method to fetch the list of files and directories in the specified path.

2. Creates a dictionary for each feedback file. The dictionary has the following structure:
   ```json
   {
       "title": "Feedback Title",
       "name": "Sender's Name",
       "date": "Date of Feedback",
       "feedback": "Actual Feedback Message"
   }
   ```
   It traverses over each file, extracts the content from these text files, and creates the corresponding dictionary using the title, name, date, and feedback as keys.

3. Uses the Python `requests` module to make a POST request to the company's website through the Django REST API. The URL to post the dictionary is `http://<corpweb-external-IP>/feedback`. Please replace `<corpweb-external-IP>` with corpweb's external IP address.

4. Ensures that an error message isn't returned during the upload process. The script checks the `status_code` and `text` of the response objects to identify any issues. A successful response has a `status_code` of 201, indicating a created success status response code.

## Requirements

- Python 3.x
- The `requests` module. You can install it using `pip install requests`.

## Important Note

Please ensure that the company's website is set up to handle the uploaded feedback data correctly. The script assumes that the website's API is ready to receive and process the data in the specified format.

**Disclaimer:** This script is intended for educational purposes and should be used responsibly with the proper authorization from the company.
