import requests
url = "http://www.google.com"
response = requests.get(url)

print(f"your request to {url} cam back with status code {response.status_code}")