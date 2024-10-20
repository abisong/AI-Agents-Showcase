import random

def customer_support(user_input):
    faq = {
        "return policy": "Our return policy allows returns within 30 days of purchase with a valid receipt.",
        "shipping": "We offer free shipping on orders over $50. Standard shipping takes 3-5 business days.",
        "product warranty": "All our products come with a 1-year limited warranty against manufacturing defects.",
        "payment methods": "We accept all major credit cards, PayPal, and Apple Pay.",
        "contact": "You can reach our customer support team at support@example.com or call 1-800-123-4567."
    }
    
    for key, value in faq.items():
        if key in user_input.lower():
            return value
    
    return "I'm sorry, I couldn't find a specific answer to your question. Please contact our customer support team for more assistance."

def marketing_campaign(user_input):
    campaign_ideas = [
        "Launch a social media contest to increase brand awareness",
        "Create a limited-time offer to boost sales",
        "Develop an email marketing series to nurture leads",
        "Partner with influencers to reach a wider audience",
        "Host a webinar to showcase your product or service"
    ]
    
    return f"Based on your input '{user_input}', here's a campaign idea: {random.choice(campaign_ideas)}"

def sales_negotiator(user_input):
    email_templates = [
        "Thank you for your interest in our product. I'd be happy to discuss how we can meet your specific needs.",
        "I understand your concerns about the price. Let me explain the value our product brings to your business.",
        "We appreciate your business and are willing to offer a 10% discount if you commit to a 12-month contract.",
        "Our product offers unique features that set us apart from competitors. Let's schedule a demo to showcase these benefits.",
        "I'm confident we can find a solution that works for both of us. Can we set up a call to discuss further?"
    ]
    
    return f"Here's a suggested email response:\n\nDear Valued Customer,\n\n{random.choice(email_templates)}\n\nBest regards,\nYour Sales Team"

def financial_portfolio(portfolio_data):
    total_value = sum(asset.asset_value for asset in portfolio_data)
    asset_allocation = {}
    
    for asset in portfolio_data:
        if asset.asset_type not in asset_allocation:
            asset_allocation[asset.asset_type] = 0
        asset_allocation[asset.asset_type] += asset.asset_value
    
    for asset_type, value in asset_allocation.items():
        asset_allocation[asset_type] = (value / total_value) * 100
    
    analysis = f"Total portfolio value: ${total_value:.2f}\n\nAsset Allocation:\n"
    for asset_type, percentage in asset_allocation.items():
        analysis += f"{asset_type}: {percentage:.2f}%\n"
    
    return analysis

def workflow_automation(tasks):
    task_summary = {
        "New": 0,
        "In Progress": 0,
        "Completed": 0
    }
    
    for task in tasks:
        task_summary[task.status] += 1
    
    return task_summary
