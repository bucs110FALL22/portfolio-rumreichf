import requests

class CatFactAPI:
  def __init__(self):
   '''
   initializes proxy class
   args: none
   '''
    self.url = f'https://meowfacts.herokuapp.com/'
    
  def get(self):
    '''
   gets the fact from the api
   args: none
   return: string
   '''
    response = requests.get(self.url)
    resp_json = response.json()
    return resp_json['data']