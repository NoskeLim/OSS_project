from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 가입한 사용자 정보를 저장할 리스트
users = []

# 게시글 데이터를 저장할 리스트
posts = []

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

@app.route('/posts', methods=['GET'])
def post_list():
    return render_template('post_list.html', posts=posts)

@app.route('/posts/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = {'title': title, 'content': content}
        posts.append(post)
        return redirect(url_for('post_list'))
    return render_template('create_post.html')

@app.route('/posts/<int:post_id>', methods=['GET'])
def view_post(post_id):
    if post_id < len(posts):
        post = posts[post_id]
        return render_template('view_post.html', post=post)
    return "Post not found"

if __name__ == '__main__':
    app.run(debug=True)
