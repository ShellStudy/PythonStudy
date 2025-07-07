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
    
def findOne(id):
    conn = dbpool.getConn()
    if conn != None:
        cur = conn.cursor()
        sql = f"select * from user where id = '{id}'"
        cur.execute(sql)
        result = cur.fetchone()
        return result
    else:
        return {}
        