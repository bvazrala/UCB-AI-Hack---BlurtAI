import fitz # for extract_text_from_pdf
import requests
from functions import Flask, request, jsonify, abort
from flask_cors import CORS
from dotenv import load_dotenv # for creating config.env and storing keys elsewhere
load_dotenv('./config.env')
import re # for json_from_string
import json # for json_from_string
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
CORS(app)  # Enable CORS
app.config['UPLOAD_FOLDER'] = '/path/to/the/uploads'  # Configure the upload folder

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def get_answer_from_chatgpt(question, context):
    full_prompt = f"Question: {question}\n\nContext: {context}"
    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={
            'Authorization': 'Bearer API_KEY',  # Replace with your actual API key
            'Content-Type': 'application/json',
        },
        json={
            'model': 'gpt-4o',  # Update this with the correct model ID
            'messages': [{"role": "system", "content": "You are a helpful assistant."},
                         {"role": "user", "content": full_prompt}]
        }
    )
    return response.json()['choices'][0]['message']['content']

def json_from_string(string):
    # Regex pattern to match a JSON object
    json_pattern = r'\{(?:[^{}]|(?R))*\}'
    
    # Search for the JSON object in the string
    match = re.search(json_pattern, string)
    
    if match:
        json_str = match.group(0)
        try:
            # Parse the JSON object
            json_obj = json.loads(json_str)
            return json_obj
        except json.JSONDecodeError:
            raise ValueError("Found JSON object is not valid")
    else:
        raise ValueError("No JSON object found in the string")


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return abort(400, description="No file part")
    file = request.files['file']
    if file.filename == '':
        return abort(400, description="No selected file")
    if file and file.filename.endswith('.pdf'):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        context = extract_text_from_pdf(file_path)
        # Example to show integration, adjust according to your needs
        response = get_answer_from_chatgpt("What is the main topic?", context)
        return jsonify({"response": response})
    else:
        return abort(400, description="Invalid file format")

if __name__ == '__main__':
    app.run(debug=True)  # Runs the application on the local development server