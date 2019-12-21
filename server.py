"""
1. Keep pinging the list of IPs (python)
2. Update people that are home (IPs that are reachable)
3. Front end makes request to backend (http://url.com/people_home)
4. Return who is home

{
    "data": [
        {
            "name": "Geon",
            "is_home": true,
        },
        {
            "name": "Mike",
            "is_home": true,
        },
        {
            "name": "Peter",
            "is_home": true,
        },
    ]
}

"""

from flask import Flask
import json
from whos_home_service import *

app = Flask(__name__)


# Update whos_home in background
update_whos_home_in_background()

@app.route("/people_home")
def who_is_home():
    return {"data" : get_whos_home()}

if __name__ == "__main__":
    app.run(host='0.0.0.0')