#!/usr/bin/env python

import pika


# Using localhost connection params
def local_host_connection():

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    return channel