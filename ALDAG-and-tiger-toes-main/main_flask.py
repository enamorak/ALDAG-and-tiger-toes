from flask import *
from getting_app import app
app = Flask(__name__)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)

@app.route('/')
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

@app.route('/teo')
def teo_page():
    return render_template("teo.html")

@app.route('/jenny')
def jenny():
    return render_template("jenny.html")

@app.route('/base')
def base():
    return render_template("base.html")    

if __name__ == '__main__':
    app.run(debug=True)