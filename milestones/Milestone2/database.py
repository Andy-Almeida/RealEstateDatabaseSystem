# Handles all the methods interacting with the database that will populate the objects modeled for this application.

import os
import pymysql.cursors

# note that your remote host where your database is hosted 
# must support user permissions to run stored triggers, procedures and functions.
db_host = os.environ["DB_HOST"] 
db_username = os.environ["DB_USER"]
db_password = os.environ["DB_PASSWORD"]
db_name = os.environ["DB_NAME"]

def connect():
    """
    This method creates a connection with your database 
    IMPORTANT: all the environment variables must be set correctly 
               before attempting to run this method. Otherwise, it
               will trown an error message stating that the attempt
               to connect to your database failed.
    """
    try:
        conn = pymysql.connect(host=db_host,
                               port=3306,
                               user=db_username,
                               password=db_password,
                               db=db_name,
                               charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
        print("Bot connected to database {}".format(db_name))
        return conn
    except:
        print("Bot failed to create a connection with your database because your secret environment variables " +
              "(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME) are not set".format(db_name))
        print("\n")

# your code here
