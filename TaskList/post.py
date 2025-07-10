import requests

page_access_token = ''
page_id = ''
message = 'Hellooo'

url = f"https://graph.facebook.com/{page_id}/feed"
params = {
    "message": message,
    "access_token": page_access_token
}

response = requests.post(url, params=params)
print(response.json())
