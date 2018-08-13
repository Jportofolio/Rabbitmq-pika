#!/usr/bin/env python

from connection import create_channel
import time

channel = create_channel()

channel.queue_declare(queue='hello')

# creating a new queue that is durable in case the broker
# exits unexpectedly
channel.queue_declare(queue='task_queue', durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done ")

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='task_queue')


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()