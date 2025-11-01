from flask import Flask, request, render_template
import os
from datetime import datetime
import json

app = Flask(__name__)

# 메시지 저장용 리스트 (실제로는 데이터베이스 사용)
messages = []

@app.route('/')
@app.route('/index')
def index():
    """메인 페이지"""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
