from flask import Flask, render_template
app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)
