from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import datetime
from werkzeug.security import generate_password_hash,  check_password_hash
from flask_login import LoginManager, UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orm_db.db'
db = SQLAlchemy(app)


class Zoos(db.Model):
    __tablename__ = 'zoos'
    zoo_id = db.Column(db.Integer, primary_key=True)
    zoo_name = db.Column(db.String(100), nullable=True)
    place = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return "<Zoos(%r, %r, %r)>" % (
                self.zoo_id, self.zoo_name, self.place
            )

class Payments(db.Model):
    __tablename__ = 'payments'
    payment_id = db.Column(db.Integer, primary_key = True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'), nullable = False)
    date = db.Column(db.String(100), nullable=False)
    sum = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Payments(%r, %r, %r, %r)>" % (
                self.payment_id, self.order_id, self.date, self.sum
            )

class Orders(db.Model):
    __tablename__ = 'orders'
    client_id = db.Column(db.Integer, db.ForeignKey('clients.client_id'), nullable=False)  
    order_id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)   
    order_date = db.Column(db.String(100), nullable=False)
    received_date = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return "<Orders(%r, %r, %r, %r, %r)>" % (
                self.client_id, self.order_id, self.price, self.order_date, self.received_date
            )


class Clients(db.Model, UserMixin):
    __tablename__ = 'clients'
    client_id = db.Column(db.Integer(), primary_key=True)
    client_name = db.Column(db.String(100))
    uname = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    manager = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return "<{}:{}>".format(self.client_id, self.uname)

class Categories(db.Model):
    __tablename__ = 'categories'
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)  
    number = db.Column(db.Integer, nullable=False)  

    def __repr__(self):
        return "<Categories(%r, %r, %r, %r)>" % (
                self.category_id, self.category_name, self.price, self.number
            )

class Basket(db.Model):
    __tablename__ = 'basket'
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'), primary_key=True, nullable=False)  
    animal_id = db.Column(db.Integer, db.ForeignKey('animals.animal_id'), primary_key=True, nullable=False)

    def __repr__(self):
        return "<Basket(%r, %r)>" % (
                self.order_id, self.animal_id
            )

class Animals(db.Model):
    __tablename__ = 'animals'
    animal_id = db.Column(db.Integer, primary_key=True) 
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'), nullable=False)
    zoo_id = db.Column(db.Integer, db.ForeignKey('zoos.zoo_id'), nullable=False) 
    nick = db.Column(db.String(100), nullable=True)
    gender = db.Column(db.String(100), nullable=False)
    height = db.Column(db.Integer, nullable=True)
    weight = db.Column(db.Integer, nullable=True) 
    birthday = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return "<Animals(%r, %r, %r, %r, %r, %r, %r, %r)>" % (
                self.animal_id, self.category_id, self.zoo_id, self.nick, self.gender, self.height, self.weight, self.birthday
            )               

class Feedback(db.Model):
    __tablename__ = 'feedback'
    feedback_id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(80), nullable=True)
    feedback = db.Column(db.String(1000), nullable=True)

    def __repr__(self):
        return "<Feedback(%r, %r, %r)>" % (
                self.feedback_id, self.uname, self.feedback
            )

db.create_all()

"""

print('*' * 100)
print()
print('ИДЕТ СОЗДАНИЕ ТЕСТОВОЙ БАЗЫ ДАННЫХ')
print()

''' ---------------------------------------- CОЗДАНИЕ ТЕСТОВОЙ БАЗЫ ДАННЫХ ----------------------------------------'''

u = Clients(client_id = 1, client_name ='Jack Well', manager ='John Smith', telephone = 89152134567)
print(repr(u))
db.session.add(u)
u = Clients(client_id = 2, client_name ='Adam Smith', manager ='Hi Magic', telephone = 89152567898)
print(repr(u))
db.session.add(u)
u = Clients(client_id = 3, client_name ='Made Hell', manager ='Paradise Jack', telephone = 89162315778)
print(repr(u))
db.session.add(u)

u = Zoos(zoo_id = 1, zoo_name = 'Cool', place = 'Sabath')
print(repr(u))
db.session.add(u)
u = Zoos(zoo_id = 2, zoo_name = 'Warmy', place = 'LA Goon')
print(repr(u))
db.session.add(u)
u = Zoos(zoo_id = 3, zoo_name = 'Werthfdk', place = 'SA FDg')
print(repr(u))
db.session.add(u)

u = Payments (payment_id = 1, order_id = 1, date = '2021-03-05', sum = 1207)
print(repr(u))
db.session.add(u)
u = Payments (payment_id = 2, order_id = 3, date = '2021-04-05', sum = 1507)
print(repr(u))
db.session.add(u)
u = Payments (payment_id = 3, order_id = 2, date = '2021-05-05', sum = 12607)
print(repr(u))
db.session.add(u)

u = Orders(client_id = 1, order_id = 3, price = 1507, order_date = '2021-04-05', received_date = '2021-04-06')
print(repr(u))
db.session.add(u)
u = Orders(client_id = 2, order_id = 1, price = 1207, order_date = '2021-03-04', received_date = '2021-03-07')
print(repr(u))
db.session.add(u)
u = Orders(client_id = 3, order_id = 2, price = 12607, order_date = '2021-05-01', received_date = '2021-05-05')
print(repr(u))
db.session.add(u)

u = Categories(category_id = 1, category_name = 'tiger amur', price = 1207, number = 1)
print(repr(u))
db.session.add(u)
u = Categories(category_id = 2, category_name = 'tiger bengal', price = 1507, number = 1)
print(repr(u))
db.session.add(u)
u = Categories(category_id = 3, category_name = 'tiger rivera', price = 12607, number = 1)
print(repr(u))
db.session.add(u)

u = Basket(order_id = 1, animal_id = 1)
print(repr(u))
db.session.add(u)
u = Basket(order_id = 2, animal_id = 2)
print(repr(u))
db.session.add(u)
u = Basket(order_id = 3, animal_id = 3)
print(repr(u))
db.session.add(u)

u = Animals(animal_id = 1, category_id = 1, zoo_id = 3, nick = 'Leo', gender = 'm', height = 127, weight = 32, birthday = '2018-05-06')
print(repr(u))
db.session.add(u)
u = Animals(animal_id = 2, category_id = 3, zoo_id = 2, nick = 'Teo', gender = 'm', height = 125, weight = 32, birthday = '2018-05-05')
print(repr(u))
db.session.add(u)
u = Animals(animal_id = 3, category_id = 2, zoo_id = 1, nick = 'Lessy', gender = 'f', height = 123, weight = 27, birthday = '2018-08-16')
print(repr(u))
db.session.add(u)

db.session.commit()

print()
print('*' * 100)
print('ВЫПОЛНЯЮТСЯ ЗАПРОСЫ К ТЕСТОВОЙ БАЗЕ ДАННЫХ')

''' ---------------------------------------- ЗАПРОСЫ К ТЕСТОВОЙ БАЗЕ ДАННЫХ ----------------------------------------'''

print()
r = db.session.execute('SELECT DISTINCT birthday FROM animals;')
print("ТЕСТ 1/7")
for a in r:
    print(a[0])

print()
r = db.session.execute('SELECT MIN(height), MAX(height) FROM animals GROUP BY weight;')
print("ТЕСТ 2/7")
for a in r:
    print(a[0])

print()
r = db.session.execute('SELECT * FROM orders where client_id = (SELECT client_id FROM clients WHERE client_name = "Hi Magic");')
print("ТЕСТ 3/7")
for a in r:
    print(a[0])

print()
r = db.session.execute('SELECT client_name, manager FROM clients where client_id IN (SELECT client_id FROM orders WHERE price > (SELECT AVG(price) from orders));')
print("ТЕСТ 4/7")
for a in r:
    print(a[0])

print()
r = db.session.execute('SELECT client_name FROM clients WHERE client_id IN (SELECT client_id FROM orders WHERE price = (SELECT MAX(price) FROM orders));')
print("ТЕСТ 5/7")
for a in r:
    print(a[0])

print()
r = db.session.execute('select client_id from orders where order_date = "2021-03-04" and client_id not in (select client_id from orders where order_date = "2021-03-03") group by client_id;')
print("ТЕСТ 6/7")
for a in r:
    print(a[0])

print()
r = db.session.execute('select count(*)  from (select client_id from orders group by client_id having count(order_id)= 1 ) as Q')
print("ТЕСТ 7/7")
for a in r:
    print(a[0]) 

"""    