from ETL.config.mysql_config import get_mysql_connection

def clean_data():
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT title FROM users LIMIT 10")
        rows = cursor.fetchall()

        # Example cleaning logic: Strip whitespace
        cleaned_rows = [(title.strip(),) for (title,) in rows]

        cursor.close()
        conn.close()

        print("✅ Data fetched and cleaned from MySQL:")
        for row in cleaned_rows:
            print(row)

        return cleaned_rows

    except Exception as e:
        print("❌ Error querying data from MySQL:", e)
        raise
