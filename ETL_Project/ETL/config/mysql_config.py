import os
from dotenv import load_dotenv
import mysql.connector

# Load .env from root project directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', '.env'))

def get_mysql_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("HOST"),
            port=os.getenv("PORT"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DB"),
        )
        return conn
    except Exception as e:
        print("Error connecting to MySQL:", e)
        raise
