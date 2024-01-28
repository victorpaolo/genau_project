from flask import Flask, render_template, request, redirect, url_for
from database import load_vokabular_from_db


app = Flask(__name__)


@app.route('/')
def hello():
    worts = load_vokabular_from_db()
    return render_template('home.html',
                          worts=worts)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)