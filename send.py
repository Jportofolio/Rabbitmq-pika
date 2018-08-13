#!/usr/bin/env python

from connection import local_host_connection

channel = local_host_connection()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World')
print(" [x] sent 'Hello World!' ")

connection.close()


