from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ciel')
def ciel():
    return render_template('ciel.html')

@app.route('/snir')
def snir():
    return render_template('snir.html')

@app.route('/etudes-sup')
def etudes_sup():
    return render_template('etudes-sup.html')

if __name__ == '__main__':
    app.run()
