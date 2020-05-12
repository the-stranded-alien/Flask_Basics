from flask import Flask, render_template, redirect, request

# __name__ == __main__
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("Form2.html")

@app.route('/about')
def about():
    return "<h1> About Page </h1>"

@app.route('/home')
def home():
    return redirect('/')

@app.route('/submit', methods = ['POST'])
def submit_data():
    if request.method == 'POST':
        no1 = int(request.form['no1'])
        no2 = int(request.form['no2'])

        return str(no1 + no2)
    return "Nothing"

if __name__ == '__main__':
    #app.debug = True
    app.run(debug = True)