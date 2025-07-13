from fastapi import APIRouter
import mariadb
import os

ctr = APIRouter(prefix='/movie')

@ctr.get("/")
def home():
    conn_params = {
        "user" : os.getenv('MARIADB_USER'),
        "password" : os.getenv('MARIADB_PASSWORD'),
        "host" : os.getenv('MARIADB_HOST'),
        "database" : os.getenv('MARIADB_DATABASE'),
        "port" : int(os.getenv('MARIADB_PORT'))
    }
    conn = mariadb.connect(**conn_params)
    cur = conn.cursor()
    sql = "select * from movies"
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return {"movies": result}

@ctr.get("/country")
def country(name):
    conn_params = {
        "user" : os.getenv('MARIADB_USER'),
        "password" : os.getenv('MARIADB_PASSWORD'),
        "host" : os.getenv('MARIADB_HOST'),
        "database" : os.getenv('MARIADB_DATABASE'),
        "port" : int(os.getenv('MARIADB_PORT'))
    }
    conn = mariadb.connect(**conn_params)
    cur = conn.cursor()
    sql = f"SELECT * FROM movies WHERE country LIKE '%{name}%'"
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return {"result": result}
