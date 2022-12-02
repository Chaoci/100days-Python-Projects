from flask import Flask, render_template
import requests
import pandas as pd
import datetime as dt
from class_api import News, NBA
from nba_api.live.nba.endpoints import scoreboard
## for secure
import os
appid = os.getenv("APPID")
news = os.getenv("NEWS")
lat = os.getenv("LAT")
lon = os.getenv("LON")

## date
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
# date = f"{now.year} {mon[now.month]} {now.day}"

## weather api
endpoint = "https://api.openweathermap.org/data/2.5/weather?"
lang = "zh_TW"
parameters = {
    "lat":lat,
    "lon":lon,
    "appid":appid,
    "lang":lang,
}

## news api
news_endpoint = "https://newsapi.org/v2/top-headlines?"
news_parameters = {
    "country":"us",
    "apiKey":news,
}

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def get_all_posts():
    # date
    now = dt.date.today()
    date = f"{now.year} {mon[now.month]} {now.day}"
    a= requests.get(endpoint,params=parameters)
    data = a.json()
    min_temp = round(data['main']['temp_min'] - 273.15,1)
    max_temp = round(data['main']['temp_max'] - 273.15,1)
    
    #news api
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
    
    #nba api
    games = scoreboard.ScoreBoard()
    nba_data_list = []
    nba_data = games.get_dict()
    for nbapost in nba_data['scoreboard']['games']:
        nba_obj = NBA(
            homeTeam=nbapost['homeTeam']['teamName'],
            awayTeam=nbapost['awayTeam']['teamName'],
            homescore=nbapost['homeTeam']['score'],
            awayscore=nbapost['awayTeam']['score'],
        )
        nba_data_list.append(nba_obj)
    return render_template("index.html",date = date, data=data, min_temp=min_temp,max_temp=max_temp,news_obj=news_data_list, nba_obj = nba_data_list)

if __name__ == "__main__":
    app.run(debug=True)