__author__ = 'GongXingFa'

import pika

conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = conn.channel()

channel.queue_declare(queue='test')

from datetime import datetime

print 'Start Push'
start = datetime.now()
for i in xrange(1000):
    channel.basic_publish(exchange='', routing_key='test', body='Hello World!')
channel.queue_delete(queue='test')
end = datetime.now()

print('End Push.Use:' + str(end - start))