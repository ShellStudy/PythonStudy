import mariadb
from mariadb.connectionpool import ConnectionPool
import os

conn_params = {
    "user" : os.getenv('MARIADB_USER'),
    "password" : os.getenv('MARIADB_PASSWORD'),
    "host" : os.getenv('MARIADB_HOST'),
    "database" : os.getenv('MARIADB_DATABASE'),
    "port" : int(os.getenv('MARIADB_PORT')),
    "pool_size" : 5,
    "pool_name" : "db_pool"
}
try:
    pool = ConnectionPool(**conn_params)
except mariadb.Error as e:
    print(f"접속 오류 : {e}")
    pool = None
        
def getConn():
    if pool == None:
        return None
    return pool.get_connection()
    
    