from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/warmup')
def warmup():
    return render_template('warmup.html')

@app.route('/d3')
def d3():
    return render_template('d3.html')

@app.route('/svg_I')
def d32():
    return render_template('svg_I.html')

@app.route('/svg_d3')
def d3svg():
    return render_template('svg_d3.html')

@app.route('/transition_d3')
def d3t():
    return render_template('transition_d3.html')

@app.route('/animation_ex')
def anim_ex():
    return render_template('animation_ex.html')

@app.route('/csv')
def datacsv():
    return render_template('readcsv.html')

@app.route('/d3base')
def d3base():
    return render_template('d3base.html')   
if __name__ == '__main__':
    app.run(debug= True)