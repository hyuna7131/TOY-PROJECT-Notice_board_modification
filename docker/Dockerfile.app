# Python 이미지를 기반으로 설정
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일 복사
COPY requirements.txt requirements.txt
COPY app app
COPY app.py app.py

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# Flask 앱 실행
# CMD ["flask", "run", "--host=0.0.0.0"]
CMD ["python3", "app.py"]