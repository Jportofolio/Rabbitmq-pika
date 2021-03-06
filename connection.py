#!/usr/bin/env python

import pika


# Using localhost connection params
def local_host_connection():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    return connection


# Creating a channel
def create_channel():
    connection = local_host_connection()
    channel = connection.channel()
    return channel