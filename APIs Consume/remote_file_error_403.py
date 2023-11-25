import os
import requests

url = 'https://codigofacilito.com/images/cody'  # image png

response = requests.get(url, stream=True)  # create the data flow
if response.status_code == 200:  # validate the answer
    os.makedirs('images', exist_ok=True)  # create the "images" directory if it does not exist
    file_path = os.path.join('images', 'cody.png')  # complete file path
    with open(file_path, 'wb') as file:  # create the file locally
        for chunk in response.iter_content(1024):  # iterate over the flow fragments
            file.write(chunk)  # download and save the image locally
    print("Image downloaded successfully.")
else:
    print('Error:', response.status_code, response.text)