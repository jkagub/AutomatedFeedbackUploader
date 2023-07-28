#! python

import sys
import os
import requests

def upload_feedback_to_website(corpweb_external_ip):
    feedback_dir = "data\\feedback"

    try:
        feedback_files = [f for f in os.listdir(feedback_dir) if f.endswith(".txt")]
    except FileNotFoundError as e:
        print(f"Error: {e}. The directory '{feedback_dir}' does not exist.")
        return

    for feedback_file in feedback_files:
        feedback_path = os.path.join(feedback_dir, feedback_file)

        try:
            with open(feedback_path, "r") as file:
                feedback_data = {
                    "title": file.readline().strip(),
                    "name": file.readline().strip(),
                    "date": file.readline().strip(),
                    "feedback": file.readline().strip()
                }
            
            response = requests.post(f"http://{corpweb_external_ip}/feedback", json=feedback_data)

            if response.status_code == 201:
                print(f"Feedback from {feedback_data['name']} uploaded successfully.")
            else:
                print(f"Failed to upload feedback from {feedback_data['name']}. Status code: {response.status_code}")

        except FileNotFoundError as e:
            print(f"Error: {e}. The feedback file '{feedback_file}' was not found.")
        except Exception as e:
            print(f"An error occurred while processing '{feedback_file}': {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <corpweb-external-IP>")
        sys.exit(1)

    corpweb_external_ip = sys.argv[1]
    upload_feedback_to_website(corpweb_external_ip)
