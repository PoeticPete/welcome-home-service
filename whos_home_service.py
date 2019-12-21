import os
import time

# List of people's local IP addresses
people_ips = [
    ('Peter', '192.168.1.229'),
    ('Nic', '192.168.1.245'),
    ('Emmet', '192.168.1.186'),
    ('Julia', '192.168.1.234'),
    ('Mike', '192.168.1.206'),
    ('Geon', '192.168.1.238'),
    ('Rizzo', '192.168.1.252')
]

whos_home = [
    {
        "name": "Peter",
        "is_home": True,
        "last_successful_ping": 1576899126
    },
    {
        "name": "Geon",
        "is_home": True,
        "last_successful_ping": 1576899139
    }
]

# Set last successes
last_successes = {}

for i in people_ips:
    last_successes[i[0]] = 0


for person in people_ips:
    ip = person[1]
    name = person[0]
    response = os.system("ping -t 3 -c 1 " + ip)
    if response == 0:
        last_successes[name] = int(time.time())

print(last_successes)

