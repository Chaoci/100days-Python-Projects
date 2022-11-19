from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE
class Book(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()




@app.route('/')
def home():
    with app.app_context():
        all_books = db.session.query(Book).all()
        return render_template("index.html", books=all_books)


@app.route("/add",methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # CREATE RECORD
        with app.app_context():
            new_book = Book(
                title=request.form["title"],
                author=request.form["author"],
                rating=request.form["rating"]
            )
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template("add.html")
    # form = AddBook()
    # if form.validate_on_submit():
    #     try:
    #         with open("Add-book-data.csv", mode="a", encoding="utf-8") as file:
    #             file.write(f"\n{form.book_name.data},"
    #                        f"{form.author.data},"
    #                        f"{form.rate.data}")
    #     except FileNotFoundError:
    #         with open("Add-book-data.csv", mode="w",encoding="utf-8") as file:
    #             file.write("Book Name, Author, Rate")
    #             file.write(f"\n{form.book_name.data},"
    #                        f"{form.author.data},"
    #                        f"{form.rate.data}")
    #     finally:
    #         return redirect(url_for('home'))
    
@app.route("/edit", methods=["GET", "POST"])
def edit():
    with app.app_context():
        if request.method == "POST":
            #UPDATE RECORD
            book_id = request.form["id"]
            book_to_update = Book.query.get(book_id)
            book_to_update.rating = request.form["rating"]
            db.session.commit()
            return redirect(url_for('home'))
        book_id = request.args.get('id')
        book_selected = Book.query.get(book_id)
    return render_template("edit_rating.html", book=book_selected)
    
    
@app.route("/delete",methods=["GET", "POST"])
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    with app.app_context():
        book_to_delete = Book.query.get(book_id)
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

