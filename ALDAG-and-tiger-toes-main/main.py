from flask import *
app = Flask(__name__)

@app.route('/')
def welcome_page():
    return render_template("welcome_page.html")

@app.route('/about_us')
def about_us():
    return render_template("about_us.html")

if __name__ == '__main__':
    app.run(debug = True)       