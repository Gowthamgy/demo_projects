import sys
sys.path.append('/opt/airflow')
from connection.mysql_connection import get_connection
import mysql.connector

try:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees;")
    results = cursor.fetchall()

    print("Tables in the database:")
    for row in results:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
