from flask import Flask
app = Flask(__name__)
	
@app.route('/')
def Home():
   return "<h1>Hello</h1>"
