from flask import Flask
from routes import setup_routes  

app = Flask(__name__)

# routes.py에서 라우트 등록 실행
setup_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
