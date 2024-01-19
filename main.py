from flask import Flask, jsonify

from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def Rate():
   return "Rate Guru"
 
if __name__ == "__main__":
   app.run(debug = True)