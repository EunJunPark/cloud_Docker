import os

class Config:
    # Docker에서 실행 중인지 확인
    if os.getenv('DOCKER_ENV', 'false') == 'true':
        MYSQL_HOST = os.getenv('MYSQL_HOST', 'db')  # Docker 환경에서는 'db'
    else:
        MYSQL_HOST = os.getenv('MYSQL_HOST', '127.0.0.1')  # 로컬에서는 '127.0.0.1'

    MYSQL_USER = os.getenv('MYSQL_USER', 'admin')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'admin')
    MYSQL_DB = os.getenv('MYSQL_DB', 'mydatabases')
    MYSQL_PORT = int(os.getenv('MYSQL_PORT', 3307))  # 로컬과 Docker 모두 3307 포트 사용
