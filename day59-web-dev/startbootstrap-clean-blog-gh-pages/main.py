from flask import Flask, render_template,request
import requests
import smtplib
import datetime
endpoint = "https://api.npoint.io/4cedc647e52fc72c2543"
response = requests.get(endpoint).json()
app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html",all_posts= response)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login('new.chaoci@gmail.com', 'password')
        connection.sendmail('new.chaoci@gmail.com',  'password', email_message)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in response:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)