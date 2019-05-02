import psycopg2

connectionDB = psycopg2.connect(dbname='test', user='maxi', password='123456', host='172.16.97.32')

cursor = connectionDB.cursor()

cursor.execute('SELECT "username" from account;')
