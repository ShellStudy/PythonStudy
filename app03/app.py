import mariadb
def 마리아디비():
    conn_params = {
        "user" : "study",
        "password" : "study",
        "host" : "localhost",
        "database" : "edu",
        "port" : 3306
    }
    return mariadb.connect(**conn_params)

def 입력(): 
    conn = 마리아디비()
    cur = conn.cursor()

    title = input("제목을 입력하세요.")
    desc = input("설명을 입력하세요.")

    sql = f"INSERT INTO NOTICE (`title`, `desc`) VALUE ('{title}', '{desc}')"
    cur.execute(sql)
    conn.commit()

    cur.close()
    conn.close()

while True:
    모드 = input("CRUD 중 선택하세요.")
    if 모드 == 'C':
        입력()
    else:
        break