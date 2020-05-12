from flask import Flask, render_template, redirect

# __name__ == __main__
app = Flask(__name__)

friends = ["Friend_1", "Friend_2", "Friend_3"]
num = 5

@app.route('/')
def hello():
    return render_template("jinja2.html", my_friends = friends, number = num)

@app.route('/about')
def about():
    return "<h1> About Page </h1>"

@app.route('/home')
def home():
    return redirect('/')

if __name__ == '__main__':
    #app.debug = True
    app.run(debug = True)