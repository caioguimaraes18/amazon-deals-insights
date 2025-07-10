import pandas as pd
import json
import os
import requests
from headers import key, host  


url = 'https://real-time-amazon-data.p.rapidapi.com/deals-v2'

querystring = {
    'country': 'BR',
    'categories': 'eletronic',
    'min_product_star_rating': 'ALL',
    'prince_range': 'ALL',
    'discount_range': 'ALL'
}

headers = {
    'x-rapidapi-key': key,
    'x-rapidapi-host': host
}

response = requests.get(url, headers=headers, params=querystring)
response_json = response.json()


os.makedirs('Dataset', exist_ok=True)

with open('Dataset/amazon_deals.json', 'w') as f:
    json.dump(response_json, f, indent=4)



