#!/usr/bin/env python

import sys, pika
from connection import create_channel

# passing connection channel in reference
channel = create_channel()
message = ' '.join(sys.argv[1:]) or "Hello world!"

channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2, # make message persistent
                      ))
print(" [x] Sent %r" % message)

