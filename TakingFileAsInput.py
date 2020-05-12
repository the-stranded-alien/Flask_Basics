from flask import Flask, render_template, redirect, request

# __name__ == __main__
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("Form3.html")

@app.route('/about')
def about():
    return "<h1> About Page </h1>"

@app.route('/home')
def home():
    return redirect('/')

@app.route('/submit', methods = ['POST'])
def submit_data():
    if request.method == 'POST':
        name = request.form['username']
        f = request.files['userfile']
        f.save(f.filename)
        return "<h3> Hello, {} ! Your File Is Received. </h3>".format(name)
    return "Nothing"

if __name__ == '__main__':
    #app.debug = True
    app.run(debug = True)