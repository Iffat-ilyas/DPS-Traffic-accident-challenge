import requests
import json

url = "https://dps-challenge.netlify.app/.netlify/functions/api/challenge"

# Fill in the required information
github_repo = "https://github.com/Iffat-ilyas/DPS-Traffic-accident-challenge"
email = "iffatilyas14@gmail.com"
deployed_endpoint = "https://6g81d8wj0k.execute-api.eu-north-1.amazonaws.com/beta"
notes = "During the challenge, I encountered consistent errors related to missing libraries when attempting to make the POST request after deploying my model on the AWS cloud service. The model was trained using Scikit-learn version 1.2.2, while the Lambda function had a version of 0.20.3. I attempted to resolve the issue by specifying the 1.2.2 version in the requirements.txt file, but encountered difficulties finding the module. Additionally, I tried using the 1.0.2 version, but it resulted in a large layer size that prevented successful upload. Despite exploring various solutions, I regrettably couldn't resolve the issue within the given time frame. I am submitting my work with the hope that you consider the efforts I made throughout the challenge. I am enthusiastic about the opportunity and eagerly look forward to the interview. Thank you for understanding."

# Create the JSON body
data = {
    "github": github_repo,
    "email": email,
    "url": deployed_endpoint,
    "notes": notes
}

# Make the POST request
response = requests.post(url, json=data)

# Check the response
if response.status_code == 200:
    print("POST request successful.")
else:
    print("POST request failed:", response.text)

