from app import create_app

# Flask 애플리케이션을 생성합니다.
app = create_app()

if __name__ == '__main__':
    # 개발 모드로 Flask 애플리케이션을 실행합니다.
    # 호스트는 '0.0.0.0'으로 설정하여 외부에서 접근 가능하도록 합니다.
    app.run(host='0.0.0.0', port=8000, debug=True)