from flask import Flask, render_template
from core import *
app = Flask(__name__)

@app.route('/')
def serve_index():
    return render_template('index.html')

@app.route('/thesis_db')
def serve_thesis_db():
    display_order = ['ID', 'Name']
    return render_template('all_thesis.html', data=getThesisData(), display_order=display_order)

app.run(host='0.0.0.0', port=5000, debug=False)
