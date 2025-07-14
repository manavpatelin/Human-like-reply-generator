from flask import Flask, request, jsonify, render_template
from utils.reply import generate_reply
from utils.db import store_reply
import os

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reply', methods=['GET'])
def reply_info():
    return jsonify({
        "message": "This endpoint requires a POST request",
        "required_fields": ["platform", "post_text"],
        "example": {
            "platform": "twitter",
            "post_text": "I just launched my new website!"
        }
    })

@app.route('/reply', methods=['POST'])
def generate_reply_route():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
            
        if 'platform' not in data or 'post_text' not in data:
            return jsonify({
                "error": "Missing required fields",
                "required_fields": ["platform", "post_text"]
            }), 400
            
        platform = data['platform']
        post_text = data['post_text']
        
        if not platform or not post_text:
            return jsonify({"error": "Empty values are not allowed"}), 400
            
        generated_reply = generate_reply(platform, post_text)
        
        # Still store in database but don't include status in response
        store_reply(platform, post_text, generated_reply)
        
        response = {
            "reply": generated_reply
        }
        
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=False)