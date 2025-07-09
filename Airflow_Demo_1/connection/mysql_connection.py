import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path="/opt/airflow/.env")

HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DB = os.getenv("DB")
PORT = int(os.getenv("PORT", "3306"))

config = {
    "host": HOST,
    "user": USER,
    "passwd": PASSWORD,
    "db": DB,
    "port": PORT
}

def get_connection():
    """Returns a MySQL connection object."""
    return mysql.connector.connect(**config)
