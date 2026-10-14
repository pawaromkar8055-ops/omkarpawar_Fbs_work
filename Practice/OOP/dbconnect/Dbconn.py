##step 1

import mysql.connector as c
con=c.connect(
    host='localhost',
    user='root',
    password='pass123',
    database="JulyPython"
)
# if con.is_connected:
#     print("Suusess")
# else:
#     print("Kusch to gadabad hai")

cursor=con.cursor()
# cursor.execute("CREATE DATABASE JulyPython") 
# cursor.execute('CREATE TABLE Emp(eid int,ename varchar(100))')
# d=cursor.execute('show tables')
# for i in cursor:
#     print(i)
# qury="insert into emp(eid,ename)values('%s',%s)"
# value=(17,"Rahul")
# cursor.execute(qury,value) # for excute one by one values

# value=[(17,"Rahul"),(45,"Rohit"),(18,"Virat")]
# cursor.executemany(qury,value) # for excute so many values at a time 

# print(cursor.rowcount,"Afected")
# con.commit()

##++++ select ++++++
# cursor.execute("SELECT * FROM emp")
# d=cursor.fetchall() # for all data select form table
# d=cursor.fetchone() # fro one data select from table
# print(d)
# for i in d: # print all data one by one
#     print(i)
    
##++++++++ update +++++++
# q='update emp set ename=%s where eid = %s'
# val=("jadhav",13) # for one values update
# cursor.execute(q,val)

# val=[("smriti",18),("kranti",45)] # for more value update
# cursor.executemany(q,val)
# print(cursor.rowcount,"is Afected")
# con.commit()

##++++++ delete ++++++++++++
# qd='delete from emp where eid = %s'
# val=(45,)
# cursor.execute(qd,val)
# con.commit()
# print(f'{cursor.rowcount} Row is Affected...')


con.close()