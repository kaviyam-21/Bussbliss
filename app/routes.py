from flask import render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from . import db, login_manager, create_app
from .models import User
from .forms import LoginForm

# Create an instance of the app
app = create_app()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data, role=form.role.data).first()
        if user and user.password == form.password.data:  # Simple password check
            login_user(user)
            if user.role == 'crew':
                return redirect(url_for('crew_dashboard'))
            elif user.role == 'passenger':
                return redirect(url_for('passenger_dashboard'))
    return render_template('login.html', form=form)

@app.route('/crew_dashboard')
@login_required
def crew_dashboard():
    return render_template('crew_dashboard.html', user=current_user)

@app.route('/passenger_dashboard')
@login_required
def passenger_dashboard():
    return render_template('passenger_dashboard.html', user=current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
