import pymysql
from DBUtils.PooledDB import PooledDB
import time
pool = PooledDB(pymysql, 5, host='192.168.10.253', user="sa", passwd="sa", db="Car_data", port=3306, charset="utf8")
try:
    conn = pool.connection()
    cur = conn.cursor()
    sql = "select * from Car_Table "
    cur.execute(sql)
    results = cur.fetchall()
    for data in results:
        print(data)
    cur.close()
    conn.close()
except Exception :print("错误")