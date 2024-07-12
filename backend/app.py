from flask import Flask, jsonify, request
#jsonfy : JSON 응답을 쉽게 만들 수 있도록 도와주는 함수
#request : 클라이언트로부터 HTTP 요청 데이터를 다루는 객체
from flask_cors import CORS
#CORS : Flask-CORE 라이브러리로, CORS 설정을 쉽게 해준다.
from pymongo import MongoClient

app = Flask(__name__) 
#Flask 애플리케이션 인스턴스 생성
CORS(app)  # 모든 도메인에서의 접근을 허용하도록 CORS 설정 

#GET 엔트포인트 정의
@app.route('/api/data', methods=['GET'])
#GET 요청이 들어오면 실행되는 함수
def get_data():
    return jsonify({'message': 'Hello from Flask!'})

#POST 엔드포인트 정의
@app.route('/api/data', methods=['POST'])
#POST 요청 들어오면 실행되는 함수
def save_data():
    #요청의 본문에서 JSON 데이터를 가져와서 'data' 변수에 저장
    data = request.jsonfy
    #서버 콘솔에 수신된 데이터를 출력
    print(f"Received data: {data}")
    return jsonify({'status': 'success', 'data': data})

if __name__ == '__main__':
    app.run(debug=True)
