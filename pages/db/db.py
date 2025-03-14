import mysql.connector
from config import Config

# MySQL 데이터베이스 연결 (dictionary=True 추가)
db = mysql.connector.connect(
    host=Config.MYSQL_HOST,
    user=Config.MYSQL_USER,
    password=Config.MYSQL_PASSWORD,
    database=Config.MYSQL_DB,
    port=Config.MYSQL_PORT
)
cursor = db.cursor(dictionary=True)
