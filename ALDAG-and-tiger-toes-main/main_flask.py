from flask import *
app = Flask(__name__)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)

@app.route('/')
def welcome_page():
    return render_template("welcome_page.html")

@app.route('/about_us')
def about_page():
    return render_template("about_us.html")

@app.route('/catalog')
def catalog_page():
    return render_template("catalog.html")

@app.route('/in')
def in_page():
    return render_template("in.html")

@app.route('/yan')
def yan_page():
    return render_template("yan.html")

@app.route('/teo')
def teo_page():
    return render_template("teo.html")

@app.route('/jenny')
def white_jasmine_page():
    return render_template("jenny.html")

if __name__ == '__main__':
    app.run(debug=True)