#!/usr/bin/env python

import os

from rich import print
from scrapli import Scrapli

# Create device dict()
device = {
    "host": "nebula.packetflow.co.uk",
    "port": 9001,
    "auth_username": os.getenv("LAB_USERNAME"),
    "auth_password": os.getenv("LAB_PASSWORD"),
    "auth_strict_key": False,
    "platform": "cisco_nxos",
}

# Scrapli context manager - Instantiate, open and close connection
with Scrapli(**device) as conn:
    # Send config commands to device
    commands = ["interface loopback1000", "description # Scrapli Demo"]
    multiresponse = conn.send_configs(commands)

# Print MultiResponse attributes
print(multiresponse.result)
print(multiresponse.failed)

# Print Response attributes
print("---")
for response in multiresponse:
    print(f"{response.channel_input} = elapsed_time {response.elapsed_time}")
