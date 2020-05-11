from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/scatter')
def scatter():
    return render_template('d3scatter.html')

@app.route('/array')
def arrayd3():
    return render_template('d3array.html')

@app.route('/scatterplot')
def scatt():
    return render_template('d3scatt.html')

if __name__ == '__main__':
    app.run(debug=True)
