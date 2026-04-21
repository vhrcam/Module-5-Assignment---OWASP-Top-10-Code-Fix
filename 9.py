url = input("Enter URL: ")
response = requests.get(url)
print(response.text)

#fix
from urllib.parse import urlparse
import requests

ALLOWED_DOMAINS = ["example.com"]

url = input("Enter URL: ")
parsed = urlparse(url)

if parsed.hostname in ALLOWED_DOMAINS:
    response = requests.get(url)
    print(response.text)
else:
    print("Blocked request")