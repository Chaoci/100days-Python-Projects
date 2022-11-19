from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")
    
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

    
##CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

# with app.app_context():
#     db.create_all()
    
# with app.app_context():
#     new_movie = Movie(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favourite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg")
#     db.session.add(new_movie)
#     db.session.commit()

@app.route("/")
def home():
    #This line creates a list of all the movies sorted by rating
    all_movies = Movie.query.order_by(Movie.rating).all()
    
    #This line loops through all the movies
    for i in range(len(all_movies)):
        #This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    with app.app_context():
        db.session.commit()
    return render_template("index.html", movies=all_movies)

# @app.route("/add",methods=["GET", "POST"])
# def add():
#     if request.method == "POST":
#         # CREATE RECORD
        
#             return redirect(url_for('home'))
#     return render_template("add.html")


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()
    if form.validate_on_submit():
        endpoint = 'https://api.themoviedb.org/3/search/movie?'
        parameters = {
            "api_key":'9fbf464bbe1d4cd9124bbd65760617f1',
            "query":form.title.data,
        }
        response = requests.get(endpoint, params=parameters)
        response.raise_for_status
        response.json()
        data = response.json()['results']
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)

@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    # 這個with app.app_context()才能讓sqlite3正常運作
    with app.app_context():
        # find the id
        movie_id = request.args.get("id")
        # get the id 
        movie = Movie.query.get(movie_id)
        #change content
        if form.validate_on_submit():
            movie.rating = float(form.rating.data)
            movie.review = form.review.data
            db.session.commit()
            return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete",methods=["GET", "POST"])
def delete():
    movie_id = request.args.get("id")
    # DELETE A RECORD BY ID
    with app.app_context():
        movie_to_delete = Movie.query.get(movie_id)
        db.session.delete(movie_to_delete)
        db.session.commit()
        return redirect(url_for('home'))
    
    
@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{'https://api.themoviedb.org/3/movie/'}{movie_api_id}?"
        #The language parameter is optional, if you were making the website for a different audience 
        #e.g. Hindi speakers then you might choose "hi-IN"
        response = requests.get(movie_api_url, params={"api_key": '9fbf464bbe1d4cd9124bbd65760617f1', "language": "en-US"})
        data = response.json()
        with app.app_context():
            new_movie = Movie(
                title = data["title"],
                #The data in release_date includes month and day, we will want to get rid of.
                year = data["release_date"].split("-")[0],
                img_url =f"{'https://image.tmdb.org/t/p/w500/'}{data['poster_path']}",
                description=data["overview"]
            )
            db.session.add(new_movie)
            db.session.commit()
            return redirect(url_for('rate_movie', id= new_movie.id))

    
    
if __name__ == '__main__':
    app.run(debug=True,port=8000)
