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
app = Flask(__name__)

@app.route("/people_home")
def hello():
    
    return "Hello World!"

if __name__ == "__main__":
    app.run()