__author__ = 'GongXingFa'
import threading
import pika


class PopThread(threading.Thread):
    def run(self):
        conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = conn.channel()
        channel.queue_declare(queue='test')
        print 'Start Pop:' + str(threading.current_thread())
        while channel.basic_get(queue='test')[-1]:
            pass
        print 'End Pop:' + str(threading.current_thread())


for i in range(10):
    t = PopThread()
    t.start()




