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

sql = "INSERT INTO NOTICE (`title`) VALUE ('추가2 python')"
cur.execute(sql)
conn.commit()

cur.close()
conn.close()