from flask import Flask, render_template
#npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch
import requests
import pandas as pd
import datetime as dt
from news import News
## for secure
from config import appid, news, lat, lon

## date
now = dt.date.today()
mon = {
    1:'Jan',
    2:'Feb',
    3:'Mar',
    4:'Api',
    5:'May',
    6:'Jun',
    7:'Jul',
    8:'Aug',
    9:'Sep',
    10:'Oct',
    11:'Nov',
    12:'Dec'
}
date = f"{now.year} {mon[now.month]} {now.day}"

## weather api
endpoint = "https://api.openweathermap.org/data/2.5/weather?"
lang = "zh_TW"

parameters = {
    "lat":lat,
    "lon":lon,
    "appid":appid,
    "lang":lang,
}
a= requests.get(endpoint,params=parameters)
data = a.json()
min_temp = round(data['main']['temp_min'] - 273.15,1)
max_temp = round(data['main']['temp_max'] - 273.15,1)

## news api
news_endpoint = "https://newsapi.org/v2/top-headlines?"
news_parameters = {
    "country":"us",
    "apiKey":news,
}

news_data = requests.get(news_endpoint,params=news_parameters).json()
news_data_list = []
for news_post in news_data['articles'][:6]:
    news_obj = News( 
                    news_title=news_post["title"],
                    news_author=news_post["author"],
                    news_description=news_post["description"],
                    news_url = news_post["url"],
                    news_published= news_post["publishedAt"].split('T')[0]
                    )
    news_data_list.append(news_obj)


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def get_all_posts():
    return render_template("index.html",date = date, data=data, min_temp=min_temp,max_temp=max_temp,news_obj=news_data_list)

if __name__ == "__main__":
    app.run(debug=True)