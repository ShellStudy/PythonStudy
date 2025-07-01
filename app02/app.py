import mariadb

conn_params = {
    "user" : "study",
    "password" : "study",
    "host" : "localhost",
    "database" : "edu"
}

conn = mariadb.connect(**conn_params)

cur = conn.cursor()

sql = 'SELECT  `no`,  `title`,  `desc`, LEFT(`content`, 256),  `regDate`,  `modDate` FROM `edu`.`NOTICE` LIMIT 1000'
cur.execute(sql)
result = cur.fetchall()

print(result)

cur.close()
conn.close()