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

title = input("제목을 입력하세요.")
desc = input("설명을 입력하세요.")

sql = f"INSERT INTO NOTICE (`title`, `desc`) VALUE ('{title}', '{desc}')"
cur.execute(sql)
conn.commit()

cur.close()
conn.close()
