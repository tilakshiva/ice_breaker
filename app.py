from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from ice_breaker import ice_break_with

load_dotenv()

app = Flask(__name__)

@app.route(rule='/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route(rule='/process', methods=['POST']) 
def process():
    name=request.form.get('name')
    summary, image_url= ice_break_with(name=name)
    return jsonify({
        "summary": summary.to_dict(),
        "image_url": image_url
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True, port=8080)