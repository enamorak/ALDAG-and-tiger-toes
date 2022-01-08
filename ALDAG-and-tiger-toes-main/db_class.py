import sqlite3
from sqlite3 import Error

class db():

    # инициализация БД
    def __init__(self, path : str):
        self.connection = None
        try:
            self.connection = sqlite3.connect(path)
            self.cursor2 = self.connection.cursor()
            print("The connection to SQLite DB is successful")
        except Error as e:
            print(f"The error '{e}' occurred")

    @property
    def set_connection(self):
        return self.connection

    @property
    def set_cursor(self):
        return self.cursor2         

    # вывести только уникальные значения дней рождений животных
    def Distinct_birthdays(self):
            r = " SELECT DISTINCT birthday FROM animals; "
            return self.cursor2.execute(r).fetchall()
            

    # разделить животных на группы по весу и для каждой группы найти минимальный и максимальный рост
    def Divide_by_weight(self):
            r = "SELECT MIN(height), MAX(height) FROM animals GROUP BY weight;"
            return self.cursor2.execute(r).fetchall()        

    # найти все заказы определенного клиента по имени
    def Find_by_name(self, name : str):
            r = "SELECT * FROM orders where client_id = (SELECT client_id FROM clients WHERE client_name = :name);"
            return self.cursor2.execute(r, {'name': name}).fetchall()

    # вывести имена покупателей, которые имеют заказы с суммой выше средней, и менеджеров, работающих с ними
    def Find_Clinets_and_Managers(self):
            r = "SELECT client_name, manager FROM clients where client_id IN (SELECT client_id FROM orders WHERE price > (SELECT AVG(price) from orders));"
            return self.cursor2.execute(r).fetchall()

    # вывести имена всех клиентов, совершивших заказы на максимальную сумму
    def Find_Clinets_With_Max_Sum(self):
            r = "SELECT client_name FROM clients WHERE client_id IN (SELECT client_id FROM orders WHERE price = (SELECT MAX(price) FROM orders));"
            return self.cursor2.execute(r).fetchall()

    # вывести id клиентов, которые заказали что-то в один день, но не заказали ничего в другой день
    def Ordered_And_Not(self, order_datik: str):
            r = "select client_id from orders where order_date = :order_datik and client_id not in (select client_id from orders where order_date = :order_datik) group by client_id;"
            return self.cursor2.execute(r, {'order_datik': order_datik}).fetchall()

    # определить количество клиентов, совершивших только n заказов
    def N_Orders(self, n: int):
            r = "select count(*)  from (select client_id from orders group by client_id having count(order_id)= :n ) as Q"
            return self.cursor2.execute(r, {'n': n}).fetchall()                      


# использование класса
base = db("ALDAG-and-tiger-toes-main/base2.db")
base.Distinct_birthdays()
base.Divide_by_weight()
base.Find_by_name("Well Well")
base.Find_Clinets_and_Managers()
base.Find_Clinets_With_Max_Sum()
base.N_Orders(3)
base.Ordered_And_Not("2021-09-01")
del base