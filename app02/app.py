import mariadb

conn_params = {
    "user" : "study",
    "password" : "study",
    "host" : "localhost",
    "database" : "edu"
}

conn = mariadb.connect(**conn_params)

cur = conn.cursor()

sql = 'SELECT  * FROM `edu`.`NOTICE` WHERE NO = 1'
cur.execute(sql)
result = cur.fetchone()

col_name = cur.description
name = ""
for row in col_name:
    name += row[0] + ("\t\t\t" if row[0] == 'regDate' else "\t")
print(name)

if result == None:
    print("데이터가 없습니다.")
else:
    행 = ""
    # print('no\ttitle\tdesc\tcontent\tregDate\t\t\tmodDate')
    for col in result:        
        if col == None:
            행 += "없다\t"
        else:
            행 += f'{col}\t'
    print(행)

cur.close()
conn.close()