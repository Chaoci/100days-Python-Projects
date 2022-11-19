from flask import Flask, render_template
import random 
import datetime
import requests
app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1,10)
    year = datetime.datetime.now().year
    return render_template('home.html',num = random_number,year = year)

@app.route('/guess/<name>')
def api(name):
    gender_endpoint = "https://api.genderize.io?"
    endpoint = "https://api.agify.io?"
    parameters = {
        'name':name,
    }
    r_response = requests.get(gender_endpoint,params=parameters)
    response = requests.get(endpoint,params=parameters)
    response.raise_for_status
    data = response.json()
    data1 = r_response.json()
    gender = data1['gender']
    n = data['name']
    age = data['age']
    return render_template('index.html', age = age, name = n,gender =gender)

if __name__ == "__main__":
    app.run(debug=True)