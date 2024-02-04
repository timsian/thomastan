from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    # You can implement your chatbot logic here, processing user_message and generating a response.
    # For simplicity, let's echo the user's input.
    bot_response = f"You said: {user_message}"
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
