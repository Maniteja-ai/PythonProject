from flask import Flask, render_template, request
from post import Post
from smtplib import SMTP

post = Post()

app = Flask(__name__)
EMAIL = "maniteja4137@gmail.com"
PASSWORD = "u18me141"

@app.route("/")
def home():
    return render_template("index.html", posts=post.all_post)

@app.route("/about")
def about_page():
    return render_template("about.html")

# @app.route("/contact")
# def contact_page():
#     return render_template("contact.html")

@app.route("/blog/<int:num>")
def post_page(num):
    post_details = post.all_post[num]
    return render_template("post.html", title=post_details['title'], subtitle=post_details["subtitle"],
                           body=post_details["body"])


@app.route("/contact", methods=["GET", "POST"])
def receive_data():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone_num = request.form["phone_number"]
        short_msg = request.form["msg"]
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            msg1 = f"Subject: New Message\n\nName:{name}\n Email:{email}\n Phone number:{phone_num}\n Message:{short_msg}"
            connection.sendmail(from_addr=EMAIL, to_addrs="maniteja2677@gmail.com", msg=msg1)
        return render_template("contact.html", msg="Successfully sent your message")
    else:
        return render_template("contact.html", msg="Contact Me")




if __name__ == "__main__":
    app.run(debug=True)

