import requests

url = 'http://localhost:8180/toggle/servo'

try:
    response = requests.get(url, timeout=500)  # Adjust the timeout value as needed
    response.raise_for_status()  # Check for HTTP errors
    print("Request successful")
except requests.Timeout:
    print("Request timed out. Check network connectivity.")
except requests.RequestException as e:
    print(f"Request failed: {e}")
