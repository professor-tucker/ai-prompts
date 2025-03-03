from flask import Flask, request, render_template
from llm_agent import LLM_Agent

app = Flask(__name__)

# Initialize the LLM Agent
agent = LLM_Agent()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Process form data
        form_data = request.form
        agent.setup_siem(form_data)
        return 'SIEM setup in progress...'
    return render_template('index.html')

if __name__ == '__main__':
    # Run the application with a non-root user
    app.run(host='0.0.0.0', port=5000)
