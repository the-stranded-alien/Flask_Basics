from flask import Flask, render_template, redirect

# __name__ == __main__
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/about')
def about():
    return "<h1> About Page </h1>"

@app.route('/home')
def home():
    return redirect('/')

if __name__ == '__main__':
    #app.debug = True
    app.run(debug = True)