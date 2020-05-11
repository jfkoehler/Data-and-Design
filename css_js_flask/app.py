from flask import Flask, render_template, request, jsonify
import requests 
app = Flask(__name__)

examples = [(i, 'ex' + str(i)) for i in range(10)]

@app.route('/')
def home():
    return render_template('home.html', examples = examples)


@app.route('/ex0')
def ex0():
    return render_template('ex0.html')

@app.route('/ex1')
def ex1():
    return render_template('ex1.html')

@app.route('/ex2')
def ex2():
    return render_template('ex2.html')

@app.route('/ex3')
def ex3():
    return render_template('ex3.html')

@app.route('/ex4')
def ex4():
    return render_template('ex4.html')

@app.route('/ex5')
def ex5():
    return render_template('ex5.html')

@app.route('/ex6')
def ex6():
    return render_template('ex6.html')

@app.route('/ex7')
def ex7():
    return render_template('ex7.html')

@app.route('/ex8')
def ex8():
    return render_template('ex8.html')

@app.route('/ex9')
def ex9():
    return render_template('ex9.html')



    

if __name__ == '__main__':
    app.run(debug = True)