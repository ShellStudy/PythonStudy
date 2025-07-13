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

def login():
    conn = connect()
    cur = conn.cursor()
    
    # 아이디와 비밀번호를 입력 받아 존재 여부 확인 후 존재 한다면 사용자 번호를 리턴해주세요.
    no = 0
    id = input("아이디를 입력하세요.")
    pwd = input("비밀번호를 입력하세요.")
    sql = f"SELECT no, pwd FROM USER WHERE id = '{id}'"
    cur.execute(sql)
    result1 = cur.fetchone()
    
    sql = f"SELECT PASSWORD('{pwd}') as pwd"
    cur.execute(sql)
    result2 = cur.fetchone()
    
    if result1 != None:
        if result1[1] == pwd or result1[1] == result2[0]:
            no = result1[0]
        
    cur.close()
    conn.close()
    return no

def check(no):
    if no > 0:
        print('로그인이 성공 하였습니다.')
    else:
        print('로그인이 실패 하였습니다.')

def run():    
    if input("환영합니다. 로그인를 하시겠습니까?(Y/N)") == 'Y':
      check(login())
    print("종료 됩니다.")
        
run()