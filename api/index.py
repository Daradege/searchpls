from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('index.html')

@app.route('/')
def home():
    if request.args.get('q'):
        return render_template('search.html', q=request.args.get('q'))
    return render_template('index.html')

@app.route('/search')
def search():
    q = request.args.get('q')
    return redirect(f'https://google.com/search?q={q}')