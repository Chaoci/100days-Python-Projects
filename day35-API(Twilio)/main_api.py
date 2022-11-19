import requests
import json
import pandas as pd
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token in Account Info
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC35f4156180af2487aa16f12c54e35ecd'
auth_token = 'a24b92f2c8df9f69a719c75743d779ba'


api_key = "69f04e4613056b159c2761a9d9e664d2"
lat = 22.3377
lon= 125.1236
part = "current,minutely,daily"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
parameters = {
    "lat":lat,
    "lon":lon,
    "appid": api_key,
    "exclud":part, 
}

# response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}")

response_1 = requests.get(OWM_Endpoint,params=parameters)

response_1.raise_for_status()

# response.raise_for_status()
data = response_1.json()
# data['hourly'][0]['weather'][0]['id']

data_slice = data["hourly"][:12]

will_rain = False
for hour_data in data_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='Hi there, It\'s going to rain today. Remember to bring an ☔️.',
        from_='+12136006119',
        to='+886930222895'
    )
    print(message.status)