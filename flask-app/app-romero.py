from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	return "lets go ça fonctione pas ou peut etre que si stp"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
