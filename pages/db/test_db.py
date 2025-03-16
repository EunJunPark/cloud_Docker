import mysql.connector

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="admin",
        password="admin",
        database="mydatabases",
        port=3307,
        auth_plugin='mysql_native_password'
    )
    print(" MySQL 연결 성공")
    conn.close()
except mysql.connector.Error as err:
    print(f" MySQL 연결 실패: {err}")
