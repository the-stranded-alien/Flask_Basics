from flask import Flask, render_template

# __name__ == __main__
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/about')
def about():
    return "<h1> About Page </h1>"

if __name__ == '__main__':
    #app.debug = True
    app.run(debug = True)