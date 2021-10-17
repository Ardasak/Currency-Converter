import requests

from wx.core import ACC_STATE_SYSTEM_READONLY


def get_data(first_currency,second_currency,amount):
  
    url = f"https://api.frankfurter.app/latest?from={first_currency}&to={second_currency}"
    
    response = requests.get(url)
    jsonverisi=response.json()

    return str(jsonverisi["rates"][second_currency]*amount)
    