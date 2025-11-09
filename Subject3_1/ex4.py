from flask import Flask, render_template, request

app = Flask(__name__)

# 팀원별 담당 모듈을 클래스로 구성
class TeamMember:
    """팀원 기본 클래스"""
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def process_data(self, data):
        """각 팀원이 오버라이드할 메서드"""
        pass

class BasicMember(TeamMember):
    """기본 담당 - Name, Student Number 처리 (리더가 담당)"""
    def process_data(self, data):
        result = {}
        if 'name' in data:
            result['name'] = data['name']
        if 'student_number' in data:
            result['student_number'] = data['student_number']
        if 'email' in data:
            result['email'] = data['email']    
        return result

class Member1(TeamMember):
    """팀원1 - Gender, Major 처리"""
    def process_data(self, data):
        result = {}
        if 'gender' in data:
            result['gender'] = data['gender']
        if 'major' in data:
            result['major'] = data['major']
        return result
class Member2(TeamMember):
    """팀원2 - Programming Languages 처리"""
    def process_data(self, data):
        result = {}
        # data는 request.form 이 들어오므로 getlist 사용 가능
        languages = data.getlist('languages')
        result['languages'] = ', '.join(languages) if languages else 'None'
        return result
class Member3(TeamMember):
    """팀원3 - Field, Framework 처리"""
    def process_data(self, data):
        result = {}
        result['field'] = data.get('field', '선택안함')
        framework = data.getlist('framework')
        result['framework'] = ', '.join(framework) if framework else 'None'
        return result

# 팀원 인스턴스 생성
team_members = {
    'leader': BasicMember('오지원', 'Name & Student Number Handler'),
    'member1': Member1('조혜림', 'Gender & Major Handler'),
    'member2': Member2('장서준', 'Programming Languages Handler'),
    'member3': Member3('김태훈', 'Field & Framework Handler')
}

@app.route('/')
def input_page():
    """입력 페이지 렌더링"""
    return render_template('input.html')

@app.route('/result', methods=['POST'])
def result_page():
    """결과 페이지 렌더링"""
    all_results = {}
    
    # 리더(기존 basic) 처리
    leader_data = team_members['leader'].process_data(request.form)
    all_results.update(leader_data)
    
    # 팀원1 처리
    member1_data = team_members['member1'].process_data(request.form)
    all_results.update(member1_data)
    
    # 팀원2 처리
    member2_data = team_members['member2'].process_data(request.form)
    all_results.update(member2_data)

    # 팀원3 처리 
    member3_data = team_members['member3'].process_data(request.form)
    all_results.update(member3_data)
    
    return render_template('result.html', data=all_results)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
