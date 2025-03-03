from flask import Flask, request, render_template
from llm_agent import LLM_Agent
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

# Initialize the LLM Agent
agent = LLM_Agent()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Process form data
        form_data = request.form
        logging.info('Received form data: %s', form_data)
        agent.setup_siem(form_data)
        return 'SIEM setup in progress...'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
