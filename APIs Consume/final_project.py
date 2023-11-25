import requests
import webbrowser

from setting import client_id
from setting import secret_id

# get the code
def get_url_code():
   url = 'https://github.com/login/auth/authorize'
   params = {
      'client_id':client_id,
      'scope':'user'
   }
   
   response = requests.get(url, params=params)
   return response.url

def get_access_token(code):
   url = 'https://github.com/login/auth/acces_token'
   params = {
      'client_id':client_id,
      'client_secret':secret_id,
      'code':code
   }
   
   headers = {'Accept': 'application/json'}
   
   response = requests.post(url, params= params, headers=headers)
   
   if response.status_code == 200:
      payload = response.json()
      return payload.get('access_token')
   
   # user authentication
   def get_user(access_token):
      url = 'http://api.github.com/user'
      
      headers = {
         "Accept": "application/vnd.github+json",
         "Authorization": f"Bearer {access_token}"
      }
      
      response = requests.get(url, headers=headers)
      if response.status_code == 200:
         return response.json()
         
         
      if __name__== '__main__':
         
         url = get_url_code()
         webbrowser.open(url)
         
         code = input('Enter your access code: ')
         code = code.strip().replace('\n', '')
         
         access_token = get_access_token(code)
         print(access_token)
         
         
         user = get_user(access_token)
         print(user)