import requests
from pprint import pprint


#{'key': 'ee3f377698dc4bc77431164a085bbc434683154b'}

def client():
    credentials = {
        'username': 'normal1',
        'email': 'normal@gmail.com',
        'password1': 'N123321!',
        'password2': 'N123321!'
    }
    
    response = requests.post(
        url = 'http://127.0.0.1:8000/api/rest-auth/registration/',
        data = credentials,
        
    )
    
    print('Status Code:', response.status_code)
    
    response_data = response.json()
    pprint(response_data)
    
    
if __name__ == '__main__':
    client()