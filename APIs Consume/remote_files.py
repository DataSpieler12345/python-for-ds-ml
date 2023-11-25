# downloading remote files

import requests

url = 'https://codigofacilito.com/images/cody' # image png

response = requests.get(url, stream=True) #create the tunnel stream

if response.status_code == 200: # validating the response
   with open('images/cody.png', 'wb') as file: #create file locally
      for chunk in response.iter_content(1024): # iterate over the chunks
         file.write(chunk) # downloading and saving the image locally
      
   