from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables CORS for all domains on all routes

@app.route('/process_notes', methods=['POST'])
def process_notes():
    if request.method == 'POST':
        # Extract data from POST request
        data = request.json
        notes = data['notes']
        
        # Here you would typically call your function that handles the OpenAI API
        processed_data = handle_notes_with_openai(notes)

        # Return a JSON response with the processed data
        return jsonify(processed_data)

def handle_notes_with_openai(notes):
    # Dummy function for processing notes
    # Replace this with actual code to call the OpenAI API and process the notes
    return {"summary": "This is a summary of the notes", "key_points": ["Point 1", "Point 2"]}

if __name__ == '__main__':
    app.run(debug=True)  # Runs the application on the local development server
