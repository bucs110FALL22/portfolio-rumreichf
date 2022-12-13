import requests

class QuoteAPI:
  def __init__(self):
    '''
   initializes proxy class
   args: none
   '''
    self.url = f'https://api.adviceslip.com/advice'
  def get(self):
   '''
   gets the quote from the api
   args: none
   return: string
   '''
    response = requests.get(self.url)
    resp_json = response.json()
    return resp_json['slip']