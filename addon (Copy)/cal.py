from flask import Flask, render_template  # Capital F in Flask

app = Flask(__name__)  # Capital F in Flask

@app.route("/")
def portfolio():
    return render_template("first.html")  # Make sure first.html is inside 'templates/' folder

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
