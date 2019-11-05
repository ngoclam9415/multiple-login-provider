from flask import redirect, render_template, Flask

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('localhost', 5000, debug=True, ssl_context=('cert.pem', 'key.pem'))