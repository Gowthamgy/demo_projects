from ETL.config.mysql_config import get_mysql_connection

def load_data(records):
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()

        # Create table if not exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                userId INT,
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255)
            )
        """)

        for row in records:
            cursor.execute("""
                INSERT INTO users (userId, title)
                VALUES (%s, %s)
            """, (row['userId'], row['title']))

        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Data inserted into MySQL")

    except Exception as e:
        print("❌ Error inserting data into MySQL:", e)
        raise
