from flask import render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from urllib.parse import urlparse
from app import app, db
from models import Interaction, PortfolioData, WorkflowTask, User
from ai_agents import customer_support, marketing_campaign, sales_negotiator, financial_portfolio, workflow_automation
import re

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guide')
def guide():
    return render_template('guide.html')

def is_password_strong(password):
    # Check if password is at least 8 characters long
    if len(password) < 8:
        return False
    # Check if password contains at least one uppercase letter, one lowercase letter, and one number
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password) or not re.search(r'\d', password):
        return False
    return True

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if not is_password_strong(password):
            flash('Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one number.')
            return redirect(url_for('register'))
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists')
            return redirect(url_for('register'))
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists')
            return redirect(url_for('register'))
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/customer_support', methods=['GET', 'POST'])
@login_required
def customer_support_route():
    if request.method == 'POST':
        user_input = request.form['user_input']
        ai_response = customer_support(user_input)
        interaction = Interaction(agent_type='customer_support', user_input=user_input, ai_response=ai_response)
        db.session.add(interaction)
        db.session.commit()
        return render_template('customer_support.html', ai_response=ai_response)
    return render_template('customer_support.html')

@app.route('/marketing_campaign', methods=['GET', 'POST'])
@login_required
def marketing_campaign_route():
    if request.method == 'POST':
        user_input = request.form['user_input']
        ai_response = marketing_campaign(user_input)
        interaction = Interaction(agent_type='marketing_campaign', user_input=user_input, ai_response=ai_response)
        db.session.add(interaction)
        db.session.commit()
        return render_template('marketing_campaign.html', ai_response=ai_response)
    return render_template('marketing_campaign.html')

@app.route('/sales_negotiator', methods=['GET', 'POST'])
@login_required
def sales_negotiator_route():
    if request.method == 'POST':
        user_input = request.form['user_input']
        ai_response = sales_negotiator(user_input)
        interaction = Interaction(agent_type='sales_negotiator', user_input=user_input, ai_response=ai_response)
        db.session.add(interaction)
        db.session.commit()
        return render_template('sales_negotiator.html', ai_response=ai_response)
    return render_template('sales_negotiator.html')

@app.route('/financial_portfolio')
@login_required
def financial_portfolio_route():
    portfolio_data = PortfolioData.query.all()
    analysis = financial_portfolio(portfolio_data)
    return render_template('financial_portfolio.html', portfolio_data=portfolio_data, analysis=analysis)

@app.route('/workflow_automation', methods=['GET', 'POST'])
@login_required
def workflow_automation_route():
    if request.method == 'POST':
        task_name = request.form['task_name']
        assigned_to = request.form['assigned_to']
        due_date = request.form['due_date']
        new_task = WorkflowTask(task_name=task_name, assigned_to=assigned_to, status='New', due_date=due_date)
        db.session.add(new_task)
        db.session.commit()
    tasks = WorkflowTask.query.all()
    return render_template('workflow_automation.html', tasks=tasks)

@app.route('/update_task_status', methods=['POST'])
@login_required
def update_task_status():
    task_id = request.form['task_id']
    new_status = request.form['new_status']
    task = WorkflowTask.query.get(task_id)
    if task:
        task.status = new_status
        db.session.commit()
        return jsonify({'success': True})
    return jsonify({'success': False}), 404
