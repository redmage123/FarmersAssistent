# views.py

from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from ..models.models import User, Weather, Advice, Reminder
from ..services.services import WeatherService, AdviceService, ReminderService

# Create a Blueprint for this module
views_blueprint = Blueprint('views', __name__)

@views_blueprint.route('/')
def home():
    current_app.logger.info("Dashboard route was called")
    return render_template('html/home.html')

@views_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('views.dashboard'))
        else:
            flash('Invalid username or password.')
    return render_template('html/login.html')

@views_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))

@views_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        user = User(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('views.dashboard'))
    return render_template('html/register.html')

@views_blueprint.route('/dashboard')
@login_required
def dashboard():
    weather_service = WeatherService(Weather(location=current_user.location))
    weather_service.update_weather()
    advice_service = AdviceService(current_user.preferences)
    advices = advice_service.get_advice()
    reminder_service = ReminderService(current_user.reminders)
    reminders = reminder_service.get_reminders()
    return render_template('html/dashboard.html', weather=weather_service.weather, advices=advices, reminders=reminders)

