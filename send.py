#!/usr/bin/env python

from connection import local_host_connection, create_channel

# calls the connection creation func
connection = local_host_connection()

# calls the channel creation func
channel = create_channel()

# Declares and create a new queue
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World')
print(" [x] sent 'Hello World!' ")

connection.close()


