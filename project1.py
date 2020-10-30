#Tun Myat
#51705354

import pymysql

db = pymysql.connect(host='localhost',
    user='root',
    passwd='123456',
    db= 'sample_python')
cur = db.cursor()

#question 1
sql="SELECT * FROM question"
cur.execute(sql)

print("question:")
for row in cur.fetchall():  # cur.fetchall() gets all results at a time
    print(row[0],", ", row[1],", ", row[2])



#question 2
sql="SELECT A,B FROM question WHERE name='MYAT, TUN'"
cur.execute(sql)
row = cur.fetchone()        # cur.fetchone() gets one result at a time

A = row[0]
B = row[1]
sum=(A*B)+54

sql = ("""INSERT IGNORE INTO sample_python.result(name, id2d, result)
VALUES('MYAT, TUN', '54', %s)""") # %s is a place holder for inserting a variable here
cur.execute(sql, sum)



#question 3
sql="SELECT * FROM result"
cur.execute(sql)

print("result:")
for row in cur.fetchall():  # cur.fetchall() gets all results at a time
    print(row[0],", ", row[2])

db.close()
