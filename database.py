import sqlalchemy
from sqlalchemy import create_engine

db_connection_string = "mysql+pymysql://o5nhs5oxjy51u0sg3ftg:pscale_pw_lqg2qctRrAxGQSU4HJc98aNynD3UMgMbJr5GGJ9CWKO@aws.connect.psdb.cloud/genauproject?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })
