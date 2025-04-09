> **March 14th, 2025**  **12:10:09** 
> **Topics:** [[SQL L2]]
> **Tags:** #
---

**SQL Lesson 1: From Beginner to Intermediate in One Lesson**

  

**Introduction**

  

SQL (**Structured Query Language**) is the language used to **store, retrieve, and manipulate data** in relational databases. SQL is fundamental for **data analysis, web applications, and backend development**.

  

By the end of this lesson, you will understand:

1. **Basic SQL syntax**

2. **Creating and managing databases**

3. **CRUD operations (Create, Read, Update, Delete)**

4. **Filtering and sorting data**

5. **Joining multiple tables**

6. **Using aggregate functions**

7. **Intermediate SQL techniques like subqueries and indexes**

---

**1. Setting Up SQL**

  

You can use SQL with **MySQL, PostgreSQL, SQLite, SQL Server**, or **Oracle**.

To experiment locally, install **SQLite** (lightweight database) or use an **online SQL sandbox** like [SQL Fiddle](http://sqlfiddle.com/).

  

To install SQLite:

```
pip install sqlite3  # If using Python
```

To enter SQLite shell:

```
sqlite3 my_database.db
```

  

---

**2. Creating a Database and Tables**

  

**2.1. Creating a Database**

  

To create a new database:

```
CREATE DATABASE company;
```

To use the database:

```
USE company;
```

**2.2. Creating a Table**

  

Tables store data in **rows and columns**.

```
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    department VARCHAR(50),
    salary DECIMAL(10,2)
);
```

• **id**: Unique identifier (**Primary Key**)

• **name**: Stores up to 50 characters

• **age**: Stores integer values

• **department**: Text column

• **salary**: Stores decimal values (up to 10 digits, 2 decimal places)

---

**3. Inserting Data into a Table**

```
INSERT INTO employees (id, name, age, department, salary)  
VALUES (1, 'Alice', 30, 'HR', 50000.00);

INSERT INTO employees (id, name, age, department, salary)  
VALUES (2, 'Bob', 28, 'Engineering', 70000.00),
       (3, 'Charlie', 35, 'Finance', 60000.00);
```

  

---

**4. Retrieving Data (SELECT Query)**

  

**4.1. Selecting All Data**

```
SELECT * FROM employees;
```

**4.2. Selecting Specific Columns**

```
SELECT name, department FROM employees;
```

  

---

**5. Filtering Data (WHERE Clause)**

  

**5.1. Filtering by a Condition**

```
SELECT * FROM employees WHERE age > 30;
```

**5.2. Filtering with Multiple Conditions (AND, OR, NOT)**

```
SELECT * FROM employees WHERE department = 'Engineering' AND salary > 60000;
```

  

---

**6. Sorting Data (ORDER BY Clause)**

```
SELECT * FROM employees ORDER BY salary DESC;
```

• ASC → Ascending order (default)

• DESC → Descending order

---

**7. Updating Data (UPDATE Query)**

```
UPDATE employees SET salary = 75000 WHERE id = 2;
```

  

---

**8. Deleting Data (DELETE Query)**

```
DELETE FROM employees WHERE id = 3;
```

**WARNING:** Without a WHERE clause, all rows will be deleted.

---

**9. Joining Multiple Tables (JOIN Clause)**

  

**9.1. Creating Another Table**

```
CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);
```

```
INSERT INTO departments (id, name)  
VALUES (1, 'HR'), (2, 'Engineering'), (3, 'Finance');
```

**9.2. INNER JOIN (Match records in both tables)**

```
SELECT employees.name, departments.name AS department  
FROM employees  
INNER JOIN departments ON employees.department = departments.name;
```

  

---

**10. Aggregate Functions (SUM, AVG, COUNT, MIN, MAX)**

  

**10.1. Counting Employees**

```
SELECT COUNT(*) FROM employees;
```

**10.2. Calculating Average Salary**

```
SELECT AVG(salary) FROM employees;
```

**10.3. Finding Minimum and Maximum Salary**

```
SELECT MIN(salary), MAX(salary) FROM employees;
```

  

---

**11. Grouping Data (GROUP BY & HAVING Clause)**

  

**11.1. Grouping Employees by Department**

```
SELECT department, COUNT(*) AS total_employees  
FROM employees  
GROUP BY department;
```

**11.2. Filtering Grouped Results (HAVING Clause)**

```
SELECT department, AVG(salary)  
FROM employees  
GROUP BY department  
HAVING AVG(salary) > 50000;
```

  

---

**12. Subqueries (Query Inside a Query)**

```
SELECT name, salary  
FROM employees  
WHERE salary > (SELECT AVG(salary) FROM employees);
```

  

---

**13. Indexes (Optimizing Queries)**

  

Indexes speed up queries on large datasets.

```
CREATE INDEX idx_department ON employees(department);
```

  

---

**14. Constraints (Ensuring Data Integrity)**

  

**14.1. Unique Constraint**

```
CREATE TABLE users (
    id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE
);
```

**14.2. NOT NULL Constraint**

```
ALTER TABLE employees MODIFY COLUMN name VARCHAR(50) NOT NULL;
```

  

---

**15. Advanced SQL Techniques**

  

**15.1. Stored Procedures (Reusable SQL Functions)**

```
DELIMITER //
CREATE PROCEDURE GetEmployees()
BEGIN
    SELECT * FROM employees;
END //
DELIMITER ;
```

Call it using:

```
CALL GetEmployees();
```

**15.2. Triggers (Automatic Actions on Data Change)**

```
CREATE TRIGGER before_insert_employee  
BEFORE INSERT ON employees  
FOR EACH ROW  
SET NEW.salary = IF(NEW.salary < 30000, 30000, NEW.salary);
```

This ensures every new employee has at least a **$30,000 salary**.

---

**Final Project: Simple Employee Management Database**

  

**1. Create the database**

```
CREATE DATABASE company_db;
USE company_db;
```

**2. Create tables**

```
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    department VARCHAR(50),
    salary DECIMAL(10,2)
);

CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);
```

**3. Insert data**

```
INSERT INTO employees (id, name, age, department, salary)  
VALUES (1, 'Alice', 30, 'HR', 50000.00),
       (2, 'Bob', 28, 'Engineering', 70000.00);

INSERT INTO departments (id, name) VALUES (1, 'HR'), (2, 'Engineering');
```

**4. Query data**

```
SELECT employees.name, employees.salary, departments.name AS department  
FROM employees  
JOIN departments ON employees.department = departments.name;
```

  

---

**Conclusion**

  

By now, you should understand:

• **Basic SQL Syntax**

• **Creating, updating, and deleting tables**

• **Filtering and sorting data**

• **Joins, aggregations, and subqueries**

• **Indexes and stored procedures for optimization**

  

With this knowledge, you’re ready to **work with databases, build backend applications, and analyze data**. 🚀

  

🔹 **Next Step:** Learn **SQL Lesson 2** for advanced topics like **transactions, views, user permissions, and complex joins.**