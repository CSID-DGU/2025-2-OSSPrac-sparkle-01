from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def input_page():
    """입력 페이지 렌더링"""
    return render_template('input.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
