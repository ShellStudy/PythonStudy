import mariadb
from model import dbpool

def findAll():
    conn = dbpool.getConn()
    if conn != None:
        cur = conn.cursor()
        sql = "select * from user"
        cur.execute(sql)
        result = cur.fetchall()
        return result
    else:
        return []
        