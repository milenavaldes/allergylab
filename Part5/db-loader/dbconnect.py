import mysql.connector
import os
db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')

def connection():
    # Edited out actual values
    conn = mysql.connector.connect(host='dbhost',
                            port=3306,
                            database=db_name,
                            user=db_user,
                            password=db_password)
    c = conn.cursor()

    return c, conn