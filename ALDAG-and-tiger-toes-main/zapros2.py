import sqlite3
from sqlite3 import Error

# инициализация БД
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("The connection to SQLite DB is successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

# вывести только уникальные значения дней рождений животных
def Distinct_birthdays(cursor2):
        cursor2.execute(
            '''
            SELECT DISTINCT birthday FROM animals;
            '''
        )
        print(cursor2.fetchall())

# разделить животных на группы по весу и для каждой группы найти минимальный и максимальный вес
def Divide_by_weight(cursor2):
        cursor2.execute(
            '''
            SELECT MIN(height), MAX(height) FROM animals GROUP BY weight;
            '''
        )
        print(cursor2.fetchall())        

# найти все заказы определенного клиента по имени
def Find_by_name(cursor2):
        cursor2.execute(
            '''
            SELECT * FROM orders
                where client_id = (SELECT client_id FROM clients WHERE client_name = 'Well Well');
            '''
        )
        print(cursor2.fetchall())

# вывести имена покупателей, которые имеют заказы с суммой выше средней, и менеджеров, работающих с ними
def Find_Clinets_and_Managers(cursor2):
        cursor2.execute(
            '''
            SELECT client_name, manager
                FROM clients
                where client_id IN (SELECT client_id
                            FROM orders
                            WHERE price > (SELECT AVG(price)
                                        from orders));
            '''
        )
        print(cursor2.fetchall())

# вывести имена всех клиентов, совершивших заказы на максимальную сумму
def Find_Clinets_With_Max_Sum(cursor2):
        cursor2.execute(
            '''
            SELECT client_name
                FROM clients
                WHERE client_id IN (SELECT client_id
                            FROM orders
                            WHERE price = (SELECT MAX(price)
                                            FROM orders));
            '''
        )
        print(cursor2.fetchall())

# вывести id клиентов, которые заказали что-то в один день, но не заказали ничего в другой день
def Ordered_And_Not(cursor2):
        cursor2.execute(
            '''
            select client_id from orders where order_date='2021-09-01' and client_id not in
            (select client_id from orders where order_date = '2021-09-02') group by client_id; 
            '''
        )
        print(cursor2.fetchall())

# определить количество клиентов, совершивших только 1 заказ
def One_Order(cursor2):
        cursor2.execute(
            '''
            select count(*)  from (select client_id from orders group by client_id having count(order_id)=1 ) as Q
            '''
        )
        print(cursor2.fetchall())                        

if create_connection("ALDAG-and-tiger-toes-main/base2.db"):

    connection = sqlite3.connect("ALDAG-and-tiger-toes-main/base2.db")
    cursor = connection.cursor()
    
    Distinct_birthdays(cursor)
    Divide_by_weight(cursor)
    Find_by_name(cursor)
    Find_Clinets_and_Managers(cursor)
    Find_Clinets_With_Max_Sum(cursor)
    Ordered_And_Not(cursor)
    One_Order(cursor)

    connection.close()




