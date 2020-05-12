from flask import Flask

# __name__ == __main__
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World To Flask"

if __name__ == '__main__':
    #app.debug = True
    app.run(debug = True)