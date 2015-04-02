__author__ = 'GongXingFa'

import MySQLdb as mysql

import threading
import time


class MySQLThread(threading.Thread):
    def run(self):
        conn = mysql.Connection(user='root', passwd='921758', db='test')
        cur = conn.cursor()
        sql = "update image set visit_count = visit_count + 1, previous_time = last_time where s='A4-8F-3J'"
        print('Start Write:'+str(threading.current_thread()))
        for i in range(1000):
            cur.execute(sql)
            conn.commit()
            time.sleep(0.01)
        conn.close()
        print('End Write:'+str(threading.current_thread()))


for i in range(5):
    t = MySQLThread()
    t.start()
