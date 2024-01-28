from flask import Flask, render_template, request, redirect, url_for
from database import engine
from sqlalchemy import text

app = Flask(__name__)

def load_vokabular_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from genauproject.vokabular"))
  def row_to_dict(row):
    return {column: getattr(row, column) for column in row.keys()}
  worts = []
  for row in result.all():
    worts.append(row_to_dict(row))
  return worts

@app.route('/')
def hello():
    worts = load_vokabular_from_db()
    return render_template('home.html',
                          worts=worts)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)