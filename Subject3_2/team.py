from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Flash message 용도, 로컬은 의미 없으니 참고.

# 메시지 저장용 리스트 (실제로는 데이터베이스 사용)
messages = []

@app.route('/')
@app.route('/index')
def index():
    """메인 페이지"""
    return render_template('index.html')

@app.route('/input')
def input_page():
    """팀원 정보 입력 페이지"""
    return render_template('input.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """연락 페이지"""
    if request.method == 'POST':
        # 연락처 메시지 처리
        message = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'subject': request.form.get('subject'),
            'message': request.form.get('message'),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        messages.append(message)
        flash('메시지가 성공적으로 전송되었습니다!', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html', team={"name": "Sparkle"})

@app.route('/result', methods=['POST'])
def result():
    """팀원 정보 입력 결과 페이지"""
    new_member = {
        'name': request.form.get('name'),
        'role': request.form.get('role'),
        'department': request.form.get('department'),
        'phone': request.form.get('phone'),
        'email': request.form.get('email'),
        'skills': request.form.get('skills', '').split(','),
        'bio': request.form.get('bio'),
        'photo': request.form.get('photo_emoji', '👤')
    }
    
    # 개인정보 마스킹
    if new_member['phone']:
        new_member['phone'] = new_member['phone'][:-2] + '**'
    if new_member['email'] and '@' in new_member['email']:
        parts = new_member['email'].split('@')
        if len(parts[0]) > 3:
            parts[0] = parts[0][:-3] + '***'
        new_member['email'] = '@'.join(parts)
    
    return render_template('result.html', member=new_member)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
