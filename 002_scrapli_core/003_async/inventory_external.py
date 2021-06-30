import os

from scrapli.driver.core import (AsyncEOSDriver, AsyncIOSXEDriver,
                                 AsyncJunosDriver, AsyncNXOSDriver)

DEVICES = [
    {
        "auth_username": os.getenv("LAB_USERNAME"),
        "auth_password": os.getenv("LAB_PASSWORD"),
        "host": "nebula.packetflow.co.uk",
        "port": 9001,
        "transport": "asyncssh",
        "auth_strict_key": False,
        "driver": AsyncNXOSDriver,
    },
    {
        "auth_username": os.getenv("LAB_USERNAME"),
        "auth_password": os.getenv("LAB_PASSWORD"),
        "host": "nebula.packetflow.co.uk",
        "port": 9002,
        "transport": "asyncssh",
        "auth_strict_key": False,
        "driver": AsyncNXOSDriver,
    },
    {
        "auth_username": os.getenv("LAB_USERNAME"),
        "auth_password": os.getenv("LAB_PASSWORD"),
        "host": "nebula.packetflow.co.uk",
        "port": 9003,
        "transport": "asyncssh",
        "auth_strict_key": False,
        "driver": AsyncIOSXEDriver,
    },
    {
        "auth_username": os.getenv("LAB_USERNAME"),
        "auth_password": os.getenv("LAB_PASSWORD"),
        "host": "nebula.packetflow.co.uk",
        "port": 9004,
        "transport": "asyncssh",
        "auth_strict_key": False,
        "driver": AsyncIOSXEDriver,
    },
    {
        "auth_username": os.getenv("LAB_USERNAME"),
        "auth_password": os.getenv("LAB_PASSWORD"),
        "host": "nebula.packetflow.co.uk",
        "port": 9005,
        "transport": "asyncssh",
        "auth_strict_key": False,
        "driver": AsyncJunosDriver,
    },
    {
        "auth_username": os.getenv("LAB_USERNAME"),
        "auth_password": os.getenv("LAB_PASSWORD"),
        "host": "nebula.packetflow.co.uk",
        "port": 9006,
        "transport": "asyncssh",
        "auth_strict_key": False,
        "driver": AsyncJunosDriver,
    },
    {
        "auth_username": os.getenv("LAB_USERNAME"),
        "auth_password": os.getenv("LAB_PASSWORD"),
        "host": "nebula.packetflow.co.uk",
        "port": 9007,
        "transport": "asyncssh",
        "auth_strict_key": False,
        "driver": AsyncEOSDriver,
    },
    {
        "auth_username": os.getenv("LAB_USERNAME"),
        "auth_password": os.getenv("LAB_PASSWORD"),
        "host": "nebula.packetflow.co.uk",
        "port": 9008,
        "transport": "asyncssh",
        "auth_strict_key": False,
        "driver": AsyncEOSDriver,
    },
]
