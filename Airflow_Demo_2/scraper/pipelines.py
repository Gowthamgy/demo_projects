
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(dotenv_path="/opt/airflow/.env")

# Access variables
HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DB = os.getenv("DB")
PORT = int(os.getenv("PORT", "3306"))

class MySQLPipeline:
    def open_spider(self, spider):
        self.conn = mysql.connector.connect(
            host=HOST,
            user=USER,
            passwd=PASSWORD,
            db=DB,
            port=PORT,
        )
        self.cursor = self.conn.cursor()


    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
        self.cursor.execute(
            "INSERT INTO sample_table (title, email, name) VALUES (%s, %s, %s)",
            (item['title'], item['email'], item['name'])
        )
        return item
