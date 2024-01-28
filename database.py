import sqlalchemy
from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']  

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })


def load_vokabular_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from genauproject.vokabular"))
    def row_to_dict(row):
      return {column: getattr(row, column) for column in row.keys()}
    worts = []
    for row in result.all():
      worts.append(row_to_dict(row))
    return worts