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

def 읽기():
    conn = 마리아디비()
    cur = conn.cursor()
    
    sql = 'SELECT  * FROM `edu`.`NOTICE`'
    cur.execute(sql)
    result = cur.fetchall()
    
    if result == None:
        print("데이터가 없습니다.")
    else:
        for row in result:
            행 = ""
            for col in row:
                if col == None:
                    행 += "\t"
                else:
                    행 += f'{col} '
            print(행)
    
    cur.close()
    conn.close()

while True:
    모드 = input("CRUD 중 선택하세요.")
    print("="*100)
    if 모드 == 'C':
        입력()
    elif 모드 == 'R':
        읽기()
    else:
        break
    print("="*100)