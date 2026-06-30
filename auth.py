import requests
AUTH_URL = "http://4.224.186.213/evaluation-service/auth"
payload = {
    "email": "vishnuvibin813@gmail.com",
    "name": "Vishnu J",
    "rollNo": "23AIB57",
    "accessCode": "xgAsNC",
    "clientID": "YOUR_CLIENT_ID",
    "clientSecret": "YOUR_CLIENT_SECRET"
}
response = requests.post(AUTH_URL, json=payload)
print("Status Code:", response.status_code)
if response.status_code == 200:
    data = response.json()
    print("\nAccess Token:")
    print(data["access_token"])
    print("\nToken Type:")
    print(data["token_type"])
    print("\nExpires In:")
    print(data["expires_in"])
else:
    print(response.text)