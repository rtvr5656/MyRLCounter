# make tests for verify if the api key is working or not

# Status code: 200 → success
# Status code: 404 → name or platform not found or incorrect
# Status code: 401 or 403 → problem with the API_key

import requests

api_key = ""
username = ""
platform = ""

url = f""
headers = {"TRN-Api-Key": api_key}

response = requests.get(url, headers=headers)

print("Status code:", response.status_code)
print("Response:")
print(response.text)