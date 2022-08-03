import psycopg2

conn = psycopg2.connect("dbname=bank_balance_control user=evg")
cur = conn.cursor()
cur.execute("SELECT * FROM users;")
print(cur.fetchone())
