import requests

# Your fake credentials file (all fake users)
with open("phishedCreds.txt") as f:
    creds = [line.strip().split(":") for line in f]  # username:password

for username, password in creds:
    response = requests.post(
        "http://localhost:5000/submit",
        json={"username": username, "password": password}  # matches your React app
    )
    result = response.text
    print(f"[{username}] Response: {result}")

    # Optional: If login succeeds, get the flag
#    if "success" in result.lower():  # adjust based on your server response
#        otp_response = requests.get("http://localhost:5000/flag")
#        print(f"[{username}] OTP result: {otp_response.text}")

