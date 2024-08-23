import os
import pymysql
from pymysql import OperationalError
from dotenv import load_dotenv

# .env 파일에서 환경변수 로드
load_dotenv()

def get_connection():
    try:
        connection = pymysql.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            db=os.getenv('DB_NAME'),
            charset=os.getenv('DB_CHARSET'),
            cursorclass=pymysql.cursors.DictCursor,
            port=int(os.getenv('DB_PORT'))  # 포트는 int로 변환해야 함
        )
        return connection
    except OperationalError as e:
        print(f"Error: Unable to connect to the database. {e}")
        raise

# 이 함수는 데이터베이스에 연결할 때 호출됩니다.
