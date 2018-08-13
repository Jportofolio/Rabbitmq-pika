#!/usr/bin/env python

import sys
from connection import create_channel

# passing connection channel in reference
channel = create_channel()
message = ' '.join(sys.argv[1:]) or "Hello world!"

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
print(" [x] Sent %r" % message)

