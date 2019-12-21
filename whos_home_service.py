import os
import time
from threading import Thread


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


# The variable that will be send to the front end. This array will constantly be updated.
whos_home = []
whos_home_siri = {}
for i in people_ips:
    whos_home.append({
        "name": i[0],
        "is_home": False,
        "last_successful_ping": -1
    })
    whos_home_siri[i[0]] = False



# Set last successes
last_successes = {}
for i in people_ips:
    last_successes[i[0]] = -1


# Define being home as "able to ping phone within last 30 minutes (1800 seconds)"
IS_HOME_TIMEOUT = 1800

def get_whos_home():
    global whos_home
    return whos_home


def get_whos_home_siri():
    global whos_home_siri
    return whos_home_siri

def continuously_update_whos_home():
    while True:
        # Ping each person's phone
        for person in people_ips:
            ip = person[1]
            name = person[0]
            response = os.system("ping -t 1 -c 1 " + ip)
            if response == 0:
                last_successes[name] = int(time.time())

        curr_time = int(time.time())
        global whos_home
        global whos_home_siri
        whos_home.clear()

        for name in last_successes:
            is_home = (curr_time - last_successes[name] < IS_HOME_TIMEOUT)

            if is_home:
                whos_home_siri[name] = is_home

            last_successful_ping = last_successes[name]
            whos_home.append({
                "name": name,
                "last_successful_ping": last_successful_ping,
                "is_home": is_home,
            })

        print(whos_home)
        time.sleep(5)


def update_whos_home_in_background():
    thread = Thread(target = continuously_update_whos_home)
    thread.start()


