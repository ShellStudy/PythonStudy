import mariadb
import os

def connect():
    conn_params = {
        "user" : os.getenv('MARIADB_USER'),
        "password" : os.getenv('MARIADB_PASSWORD'),
        "host" : os.getenv('MARIADB_HOST'),
        "database" : os.getenv('MARIADB_DATABASE'),
        "port" : int(os.getenv('MARIADB_PORT'))
    }
    return mariadb.connect(**conn_params)

def insert(): 
    conn = connect()
    cur = conn.cursor()
    
    title = input("제목을 입력하세요.")
    desc = input("설명을 입력하세요.")
    content = input("내용을 입력하세요.")
    
    sql = f"INSERT INTO NOTICE (title, content, `desc`) VALUE ('{title}', '{content}', '{desc}')"
    cur.execute(sql)
    
    conn.commit()
    cur.close()
    conn.close()

def findAll():
    conn = connect()
    cur = conn.cursor()
    
    sql = f"SELECT no, title, `desc`, content FROM NOTICE WHERE delYn = false"
    cur.execute(sql)
    result = cur.fetchall()
    
    if result == None:
        print("데이터가 없습니다.")
    else:
        for row in result:
            print(row)
    
    cur.close()
    conn.close()
    
def findOne(no):
    conn = connect()
    cur = conn.cursor()
    
    sql = f"SELECT no, title, `desc`, content FROM NOTICE WHERE delYn = false AND no = {no}"
    cur.execute(sql)
    result = cur.fetchone()
    print(result)
    
    cur.close()
    conn.close()
    
def update():
    conn = connect()
    cur = conn.cursor()
    
    no = input("변경할 대상 번호를 입력하세요.")
    title = input("주제를 변경하세요.")
    
    sql = f"UPDATE NOTICE SET title = '{title}' WHERE no = {no}"
    cur.execute(sql)    
    
    conn.commit()
    cur.close()
    conn.close()
    
    findOne(no)
    
def delete():
    conn = connect()
    cur = conn.cursor()
    
    no = input("삭제 대상 번호를 입력하세요.")
    
    sql = f"UPDATE NOTICE SET delYn = true WHERE no = {no}"
    cur.execute(sql)        
    
    conn.commit()
    cur.close()
    conn.close()
    
def run():
    print("환영합니다.")
    while True:
        mode = input("어떤 작업을 할까요?[읽기(R), 쓰기(C), 수정(U), 삭제(D))")
        if mode == 'R':
            findAll()
        elif mode == 'C':
            insert()
        elif mode == 'U':
            update()
        elif mode == 'D':
            delete()
        else:
            break
        
run()