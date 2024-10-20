 AI Agents Showcase
Project Description
AI Agents Showcase is a web application that demonstrates the capabilities of five AI agents designed to assist businesses in various aspects of their operations. The application is built using Flask and Vanilla JS, providing a user-friendly interface to interact with these AI-powered tools.

Features
The application showcases five AI agents:

Customer Support: Provides quick answers to common customer inquiries based on a predefined FAQ.
Marketing Campaign: Generates creative campaign ideas based on product or target audience descriptions.
Sales Negotiator: Offers sample email responses for various sales scenarios to aid in negotiations.
Financial Portfolio: Provides an overview and analysis of a mock investment portfolio.
Workflow Automation: Helps manage and track tasks within a team or project.
Setup Instructions
Clone the repository:

git clone https://github.com/abisong/AI-Agents-Showcase.git
cd AI-Agents-Showcase
Install the required dependencies:

pip install -r requirements.txt
Set up the environment variables:

Create a .env file in the root directory
Add the following variables:
FLASK_SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
Initialize the database:

flask db upgrade
Run the application:

python main.py
The application will be available at http://localhost:5000.

Usage Instructions
Registration and Login
Navigate to the homepage and click on "Register" to create a new account.
After registration, log in using your credentials.
Using AI Agents
Customer Support AI Agent
Go to the Customer Support page.
Type your question in the input field.
Click "Ask" to receive an AI-generated response based on common FAQs.
Marketing Campaign AI Agent
Visit the Marketing Campaign page.
Describe your product or target audience in the text area.
Click "Generate Campaign Idea" to get an AI-generated marketing campaign suggestion.
Sales Negotiator AI Agent
Navigate to the Sales Negotiator page.
Describe a sales scenario in the text area.
Click "Generate Email Response" to receive an AI-generated email template for your sales lead.
Financial Portfolio AI Agent
Access the Financial Portfolio page.
View your mock portfolio data in the table.
Add new assets using the "Add New Asset" form.
Edit or delete existing assets using the provided buttons.
Check the AI-generated analysis and asset allocation chart for insights.
Workflow Automation AI Agent
Go to the Workflow Automation page.
Add new tasks using the "Add New Task" form.
View and update the status of existing tasks in the task list.
Use the dropdown menu to change the status of tasks (New, In Progress, Completed).
Contributing
Contributions to the AI Agents Showcase project are welcome. Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

License
This project is licensed under the MIT License. See the LICENSE file for details.
