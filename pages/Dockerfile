# Python 3.9 이미지 사용
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 패키지 목록 복사
COPY requirements.txt /app/requirements.txt

# 패키지 설치
RUN pip install -r requirements.txt

# 모든 파일 복사
COPY . /app

# Flask 앱 실행
CMD ["python", "app.py"]
