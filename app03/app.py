import mariadb
conn_params = {
    "user" : "study",
    "password" : "study",
    "host" : "localhost",
    "database" : "edu",
    "port" : 3306
}
conn = mariadb.connect(**conn_params)
cur = conn.cursor()



cur.close()
conn.close()