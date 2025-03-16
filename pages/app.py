from flask import Flask
from routes import setup_routes  
import os

app = Flask(__name__)

# app.secret_key = os.getenv('SECRET_KEY', 'my_super_secret_key')  # 환경 변수로 설정 가능

# routes.py에서 라우트 등록 실행
setup_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
