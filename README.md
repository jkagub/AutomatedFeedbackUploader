**README.md**

# Feedback Uploader Python Script

## Description

This Python script is designed to upload feedback stored in text files, all written in the same format (i.e., title, name, date, and feedback), to the company's website without having to turn it into a dictionary one by one.

## Instructions

Follow the steps below to use the feedback uploader script:

1. Place all the feedback text files in the `/data/feedback` directory.

2. Execute the Python script, passing the external IP address of the company's web server as an argument:

   ```
   python script_name.py <corpweb-external-IP>
   ```

   Replace `<corpweb-external-IP>` with the actual external IP address of the company's web server where you want to upload the feedback.

## Steps Performed by the Script

The script follows the structure below to upload the feedback:

1. Lists all `.txt` files under the `/data/feedback` directory that contains the actual feedback to be displayed on the company's website. It uses the `os.listdir()` method to fetch the list of files and directories in the specified path.

2. Checks each feedback file for validity and ensures it contains proper JSON data. If the file is empty or does not contain valid JSON, it will skip that file and print an error message.

3. Parses each feedback file's content as JSON to create a dictionary. This dictionary contains the feedback data with the keys: `"title"`, `"name"`, `"date"`, and `"feedback"`.

4. Uses the Python `requests` module to make a POST request to the company's website through the Django REST API. The URL to post the dictionary is `http://<corpweb-external-IP>/feedback`. Please replace `<corpweb-external-IP>` with corpweb's external IP address.

5. Handles server responses appropriately and prints messages for successful uploads and any encountered errors.

## Requirements

- Python 3.x
- The `requests` module. You can install it using `pip install requests`.

## Important Note

Please ensure that the company's website is set up to handle the uploaded feedback data correctly. The script assumes that the website's API is ready to receive and process the data in the specified format.

**Disclaimer:** This script is intended for educational purposes and should be used responsibly with the proper authorization from the company.