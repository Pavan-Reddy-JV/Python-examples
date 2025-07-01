import requests

header = {
    'Accept':'text/plain',
    'content_type' : 'application/json'
}

response = requests.get("https://google.com")

print(response.status_code)
print(response.json())
