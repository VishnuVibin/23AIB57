import requests
REGISTER_URL = "http://4.224.186.213/evaluation-service/register"
payload = {
    "email": "vishnuvibin813@gmail.com",
    "name": "Vishnu J",
    "mobileNo": "9486765981",
    "githubUsername": "https://github.com/VishnuVibin",
    "rollNo": "23AIB57",
    "accessCode": "xgAsNC"
}
response = requests.post(REGISTER_URL, json=payload)
print("Status Code:", response.status_code)
print("Response:")
print(response.json())