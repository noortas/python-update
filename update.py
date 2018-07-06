#!/usr/bin/env python

import mysql.connector
import os
from flask import Flask
app = Flask(__name__)

@app.route("/populate")
def hello():

    cx = mysql.connector.connect(host=os.environ.get('MYSQL_HOST'), user=os.environ.get('MYSQL_USER'), passwd=os.environ.get('MYSQL_PASSWORD'), db=os.environ.get('MYSQL_DATABASE'))
    cursor = cx.cursor()
    for x in range(1000000):
        add_user = ("INSERT INTO user "
                    "(first_name, last_name) "
                    "VALUES ('test', 'test')")
        cursor.execute(add_user)

    cx.commit()

    cursor.close()
    cx.close()

    return "Hey insert successful"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
