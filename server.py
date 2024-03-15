from flask import Flask, render_template, redirect,request
from users import User
app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/users')

@app.route("/users")
def users():
    users = User.get_all()
    return render_template("users.html", usuarios =users)
#guardar
@app.route('/user/create',methods=['POST'])
def save():
    User.save(request.form)
    return redirect('users')


if __name__ == "__main__":
    app.run(debug=True, port=8000)