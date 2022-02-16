from flask import *
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from getting_app import app
from orm import db, Clients

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orm_db.db'
db = SQLAlchemy(app)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def start_page():
    return render_template("start_page.html")

@app.route("/sign_in",methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        uname = request.form["uname"]
        password = request.form["password"]
        login = Clients.query.filter_by(uname=uname, password = password).first()
        if login is not None:
            return redirect(url_for("welcome_page"))
    return render_template("sign_in.html")

@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        client_name = request.form['client_name']
        uname = request.form['uname']
        email = request.form['email']
        password = request.form['password']

        register = Clients(client_name = client_name, uname = uname, email = email, password =  password)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("sign_in"))
    return render_template("sign_up.html")

@app.route('/welcome_page')
def welcome_page():
    return render_template("welcome_page.html")

@app.route('/about_us', methods=['GET', 'POST'])
def about_page():
    """ feedback = Feedback.query.all()
    if request.method == 'POST':
        client_name = request.form.get('client_name')
        text = request.form.get('text')
        if client_name != '' and text != '':
            feed = Feedback(client_name = client_name, text = text)
            db.session.add(feed)
            db.session.commit()
            feedback.append(feed)
    print(feedback) 
    return render_template("about_us.html", feedback = feedback) """
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

@app.route('/base')
def base():
    return render_template("base.html")    

if __name__ == '__main__':
    app.run(debug=True)