from flask import Flask, request, jsonify, render_template
from generate import analyze_sentiment

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_sentiment_api():
    data = request.json
    text = data.get('text')
    
    if not text:
        return jsonify({'error': 'Text is required'}), 400
    
    sentiment = analyze_sentiment(text)
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
