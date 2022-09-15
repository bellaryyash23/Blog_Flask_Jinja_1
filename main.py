from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    blogs_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blogs_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route("/post/<blog_id>")
def get_posts(blog_id):
    blogs_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blogs_url)
    all_posts = response.json()
    return render_template("post.html", posts=all_posts, post_id=int(blog_id))


if __name__ == "__main__":
    app.run(debug=True)
