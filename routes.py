from flask import render_template, request, jsonify
from app import app, db
from models import Interaction, PortfolioData, WorkflowTask
from ai_agents import customer_support, marketing_campaign, sales_negotiator, financial_portfolio, workflow_automation

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customer_support', methods=['GET', 'POST'])
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
def financial_portfolio_route():
    portfolio_data = PortfolioData.query.all()
    analysis = financial_portfolio(portfolio_data)
    return render_template('financial_portfolio.html', portfolio_data=portfolio_data, analysis=analysis)

@app.route('/workflow_automation', methods=['GET', 'POST'])
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
def update_task_status():
    task_id = request.form['task_id']
    new_status = request.form['new_status']
    task = WorkflowTask.query.get(task_id)
    if task:
        task.status = new_status
        db.session.commit()
        return jsonify({'success': True})
    return jsonify({'success': False}), 404
