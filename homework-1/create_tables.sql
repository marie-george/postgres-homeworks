-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employees_id smallserial PRIMARY KEY,
	first_name varchar(100) ,
	last_name varchar(100),
	title varchar (200),
	birth_date date,
	notes text
);

CREATE TABLE customers
(
    customer_id varchar(100) PRIMARY KEY,
	company_name varchar(200),
	contact_name varchar(200)
);

CREATE TABLE orders
(
    order_id smallserial PRIMARY KEY,
	customer_id varchar(100) REFERENCES customers(customer_id),
	employee_id smallserial REFERENCES employees(employees_id),
	order_date date,
	ship_city varchar(100)
);
