from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# 가입한 사용자 정보를 저장할 리스트
users = []

@app.route('/')
def index():
    return redirect('/register')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        id = request.form['id']
        password = request.form['password']
        age = request.form['age']
        location = request.form['location']
        email = request.form['email']

        # 회원 정보를 딕셔너리로 저장
        user = {
            'id': id,
            'password': password,
            'age': age,
            'location': location,
            'email': email
        }

        # 회원 정보를 저장
        users.append(user)

        # 회원가입이 완료되면 success 페이지로 리디렉션
        return redirect('/success')

    return render_template('register.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
