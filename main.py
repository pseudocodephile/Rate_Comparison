from flask import Flask, request, jsonify

app = Flask(__name__)
 
@app.route('/')
def Rate():
   return "Rate Guru"
 
if __name__ == "__main__":
   app.run(debug = True)
