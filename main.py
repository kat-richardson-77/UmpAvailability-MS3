import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database='umpavailability',
    user='postgres',
    password='catykins1977!',
    port='5432'
)

cursor = conn.cursor()

postgresql_query = "SELECT * FROM umpires"
cursor.execute(postgresql_query)
print(cursor.fetchall())