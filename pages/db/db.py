import mysql.connector
from .config import Config  # 현재 폴더 내에서 config.py를 import

def get_db():
    """ 데이터베이스 연결 생성 (요청마다 새로운 연결) """
    return mysql.connector.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DB,
        port=Config.MYSQL_PORT,
        auth_plugin='mysql_native_password'  # 인증 방식 명시

    )

def get_cursor():
    """ 데이터베이스 커서 반환 """
    db = get_db()
    return db.cursor(dictionary=True), db
