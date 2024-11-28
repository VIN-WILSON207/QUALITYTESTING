# app.py
from flask import Flask, jsonify

app = Flask(__name__) 


@app.route('/')
def home():
     # Intentionally cause a 500 Internal Server Error
    result = None
    return result.some_nonexistent_method()  # This will raise an AttributeError
    return jsonify(message="Hello level 400 FET, Quality Assurance!")


if __name__ == '__main__':
    app.run(debug=True)
    