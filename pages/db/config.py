import os

class Config:
    MYSQL_HOST = os.getenv('MYSQL_HOST', '127.0.0.1')  # 로컬에서는 '127.0.0.1' 사용
    MYSQL_USER = os.getenv('MYSQL_USER', 'admin')  # 로컬에서는 기본적으로 'root' 계정 사용
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'admin')
    MYSQL_DB = os.getenv('MYSQL_DB', 'mydatabases')
    MYSQL_PORT = int(os.getenv('MYSQL_PORT', 3306))  # 로컬 MySQL이 3307 포트에서 실행됨

# import os

# class Config:
#     MYSQL_HOST = os.getenv('MYSQL_HOST', 'mysql')  # 도커 컨테이너 내에서는 'mysql' 사용
#     MYSQL_USER = os.getenv('MYSQL_USER', 'myuser')  # root 대신 myuser 사용
#     MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '1234')
#     MYSQL_DB = os.getenv('MYSQL_DB', 'mydatabase')
#     MYSQL_PORT = int(os.getenv('MYSQL_PORT', 3307))
