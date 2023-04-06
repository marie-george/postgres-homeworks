"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
from psycopg2 import OperationalError
import csv


class DatabaseConnectionError(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = 'Ошибка подключения к базе данных'

    def __str__(self):
        return self.message


try:
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='latino87Aruba@')
except OperationalError:
    raise DatabaseConnectionError

cur = conn.cursor()

with open('../homework-1/north_data/customers_data.csv', 'r', encoding='windows-1251') as file:
    customers_data = csv.DictReader(file)
    for row in customers_data:
        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (row['customer_id'], row['company_name'], row['contact_name']))
        conn.commit()

with open('../homework-1/north_data/employees_data.csv', 'r', encoding='windows-1251') as file:
    employees_data = csv.DictReader(file)
    for id, row in enumerate(employees_data, 1):
        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (id, row['first_name'], row['last_name'],
                                                           row['title'], row['birth_date'], row['notes']))
        conn.commit()

with open('../homework-1/north_data/orders_data.csv', 'r', encoding='windows-1251') as file:
    orders_data = csv.DictReader(file)
    for row in orders_data:
        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (row['order_id'], row['customer_id'],
                                                           row['employee_id'], row['order_date'], row['ship_city']))
        conn.commit()

