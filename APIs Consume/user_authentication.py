import requests

access_token = "your code is"

url = 'https://api.github.com/user'

headers = {
   'Accept': 'application/wnd.github+json',
   'Authorization': f'Bearer {access_token}'
}
# Application on github
# user code -> query method
# request access token -> post method


response = requests.get(url, headers=headers)

if response.status_code == 200:
   username = response.json().get('login')
   
print(username)