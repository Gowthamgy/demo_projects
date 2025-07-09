
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
        
    def process_item(self, item, spider):
        self.cursor.execute(
            """
            INSERT INTO employees 
            (FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUMBER, HIRE_DATE, JOB_ID, SALARY, COMMISSION_PCT, MANAGER_ID, DEPARTMENT_ID)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                item['first_name'],
                item['last_name'],
                item['email'],
                item['phone_number'],
                item['hire_date'],
                item['job_id'],
                item['salary'],
                item['commission_pct'],
                item['manager_id'],
                item['department_id']
            )
        )
        return item


    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()

    
