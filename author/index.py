from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

app = Flask(__name__)
app.secret_key = 'your_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

# Mock database of users
class User(UserMixin):
    def __init__(self, id, username, password, role):
        self.id = id
        self.username = username
        self.password = password
        self.role = role

users = [
    User(1, 'admin', 'adminpassword', 'admin'),
    User(2, 'user', 'userpassword', 'user')
]

# User loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return next((user for user in users if user.id == int(user_id)), None)

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = next((user for user in users if user.username == username and user.password == password), None)
        if user:
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

# Dashboard route (requires login)
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
