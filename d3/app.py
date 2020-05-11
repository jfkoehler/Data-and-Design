from flask import Flask, request, render_template 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ex1')
def ex1():
    return render_template('ex1.html')

if __name__ == '__main__':
    app.run(debug = True)