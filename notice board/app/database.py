import os
import pymysql
from pymysql import OperationalError
from dotenv import load_dotenv

# .env 파일에서 환경변수 로드
load_dotenv()

def get_connection():
    try:
        connection = pymysql.connect(
            host=os.getenv('DATABASE_HOST'),
            user=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASSWORD'),
            db=os.getenv('DATABASE_NAME'),
            charset=os.getenv('DATABASE_CHARSET'),
            cursorclass=pymysql.cursors.DictCursor,
            port=int(os.getenv('DATABASE_PORT', 3306))  # 포트는 int로 변환해야 함
        )
        return connection
    except OperationalError as e:
        print(f"Error: Unable to connect to the database. {e}")
        raise