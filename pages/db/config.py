import os

class Config:
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'mysql')  # 도커 컨테이너 내에서는 'mysql' 사용
    MYSQL_USER = os.getenv('MYSQL_USER', 'myuser')  # root 대신 myuser 사용
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '1234')
    MYSQL_DB = os.getenv('MYSQL_DB', 'mydatabase')
    MYSQL_PORT = int(os.getenv('MYSQL_PORT', 3307))
