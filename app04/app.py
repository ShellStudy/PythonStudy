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
    
    sql = f""
    
    
    conn.commit()
    cur.close()
    conn.close()

def findAll():
    conn = connect()
    cur = conn.cursor()
    
    sql = f""
    
    
    cur.close()
    conn.close()
    
def findOne():
    conn = connect()
    cur = conn.cursor()
    
    sql = f""
    
    
    cur.close()
    conn.close()
    
def update():
    conn = connect()
    cur = conn.cursor()
    
    sql = f""
    
    
    conn.commit()
    cur.close()
    conn.close()
    
def delete():
    conn = connect()
    cur = conn.cursor()
    
    sql = f""
        
    
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