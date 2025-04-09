> **March 14th, 2025**  **12:10:41** 
> **Topics:** [[SQL L3]] 
> **Tags:** #
---

**SQL Lesson 2: Intermediate to Advanced SQL Mastery**

  

**Introduction**

  

Now that you understand the fundamentals of SQL, it’s time to explore **advanced database concepts** such as:

• **Transactions & ACID Properties**

• **Views**

• **Stored Procedures & Functions**

• **Triggers**

• **Window Functions**

• **CTEs (Common Table Expressions)**

• **Advanced Joins**

• **User Roles & Permissions**

• **Database Optimization**

• **NoSQL vs. SQL**

  

By the end of this lesson, you will have the skills needed to **design, optimize, and manage complex databases** effectively.

---

**1. Transactions & ACID Properties**

  

A **transaction** is a group of SQL operations executed as a single unit, ensuring **data integrity** using **ACID properties**:

• **Atomicity**: Either all statements succeed or none take effect.

• **Consistency**: Data remains valid before and after transactions.

• **Isolation**: Transactions run independently.

• **Durability**: Changes are saved permanently.

  

**1.1. Using Transactions**

```
START TRANSACTION;

UPDATE employees SET salary = salary + 5000 WHERE department = 'Engineering';

-- If everything is correct, commit the changes
COMMIT;

-- If there's an error, roll back the transaction
ROLLBACK;
```

  

---

**2. Views (Virtual Tables)**

  

A **view** is a stored SQL query that acts like a table. It **simplifies queries** and **hides complex logic**.

  

**2.1. Creating a View**

```
CREATE VIEW employee_salary AS  
SELECT name, department, salary FROM employees WHERE salary > 60000;
```

**2.2. Using a View**

```
SELECT * FROM employee_salary;
```

**2.3. Updating a View**

```
ALTER VIEW employee_salary AS  
SELECT name, department, salary FROM employees WHERE salary > 50000;
```

**2.4. Dropping a View**

```
DROP VIEW employee_salary;
```

  

---

**3. Stored Procedures & Functions**

  

A **stored procedure** is a reusable SQL block that performs operations.

  

**3.1. Creating a Stored Procedure**

```
DELIMITER //
CREATE PROCEDURE GetHighSalaryEmployees()
BEGIN
    SELECT * FROM employees WHERE salary > 70000;
END //
DELIMITER ;
```

**3.2. Calling a Stored Procedure**

```
CALL GetHighSalaryEmployees();
```

**3.3. Creating a Function**

  

Unlike procedures, **functions return a value**.

```
DELIMITER //
CREATE FUNCTION GetAverageSalary()  
RETURNS DECIMAL(10,2)  
DETERMINISTIC  
BEGIN
    DECLARE avg_salary DECIMAL(10,2);
    SELECT AVG(salary) INTO avg_salary FROM employees;
    RETURN avg_salary;
END //
DELIMITER ;
```

**3.4. Using the Function**

```
SELECT GetAverageSalary();
```

  

---

**4. Triggers (Automatic Actions on Data Change)**

  

A **trigger** is an SQL script that runs automatically before or after an event.

  

**4.1. Creating a Trigger**

```
DELIMITER //
CREATE TRIGGER before_employee_insert  
BEFORE INSERT ON employees  
FOR EACH ROW  
BEGIN
    IF NEW.salary < 30000 THEN
        SET NEW.salary = 30000;
    END IF;
END //
DELIMITER ;
```

This trigger ensures that no employee is added with a salary below **$30,000**.

---

**5. Advanced Joins**

  

Joins combine data from multiple tables.

  

**5.1. LEFT JOIN (All from Left Table + Matches from Right Table)**

```
SELECT employees.name, departments.name AS department  
FROM employees  
LEFT JOIN departments ON employees.department = departments.name;
```

**5.2. RIGHT JOIN (All from Right Table + Matches from Left Table)**

```
SELECT employees.name, departments.name AS department  
FROM employees  
RIGHT JOIN departments ON employees.department = departments.name;
```

**5.3. FULL OUTER JOIN (All Data from Both Tables)**

```
SELECT employees.name, departments.name AS department  
FROM employees  
FULL OUTER JOIN departments ON employees.department = departments.name;
```

  

---

**6. Window Functions**

  

Unlike aggregate functions (SUM, AVG), **window functions** return results **without collapsing rows**.

  

**6.1. ROW_NUMBER()**

```
SELECT name, salary, ROW_NUMBER() OVER (ORDER BY salary DESC) AS rank  
FROM employees;
```

**6.2. RANK() (Handles Ties)**

```
SELECT name, salary, RANK() OVER (ORDER BY salary DESC) AS salary_rank  
FROM employees;
```

**6.3. PARTITION BY (Grouping Without Aggregation)**

```
SELECT name, department, salary,  
       AVG(salary) OVER (PARTITION BY department) AS avg_department_salary  
FROM employees;
```

  

---

**7. CTEs (Common Table Expressions)**

  

A **CTE** is a temporary result set used in a query.

  

**7.1. Using a CTE**

```
WITH HighSalary AS (
    SELECT * FROM employees WHERE salary > 70000
)
SELECT * FROM HighSalary;
```

  

---

**8. User Roles & Permissions**

  

**8.1. Creating a New User**

```
CREATE USER 'john'@'localhost' IDENTIFIED BY 'securepassword';
```

**8.2. Granting Permissions**

```
GRANT SELECT, INSERT, UPDATE ON company.* TO 'john'@'localhost';
```

**8.3. Revoking Permissions**

```
REVOKE INSERT ON company.* FROM 'john'@'localhost';
```

**8.4. Deleting a User**

```
DROP USER 'john'@'localhost';
```

  

---

**9. Database Optimization**

  

**9.1. Creating an Index (Speeds Up Queries)**

```
CREATE INDEX idx_salary ON employees(salary);
```

**9.2. Checking Query Performance**

```
EXPLAIN SELECT * FROM employees WHERE salary > 60000;
```

**9.3. Removing Unused Indexes**

```
DROP INDEX idx_salary ON employees;
```

  

---

**10. SQL vs. NoSQL**

  

**10.1. When to Use SQL (Relational Databases)**

• **Structured, tabular data**

• **Strict relationships (foreign keys)**

• **Complex queries and transactions**

  

**10.2. When to Use NoSQL (MongoDB, Firebase)**

• **Flexible, semi-structured or unstructured data**

• **Scalability (big data, distributed systems)**

• **Fast reads/writes without strict relations**

  

**10.3. Example: NoSQL in MongoDB**

```
{
  "name": "Alice",
  "department": "HR",
  "salary": 50000
}
```

MongoDB stores data in **JSON-like** documents instead of relational tables.

---

**Final Project: Advanced Employee Management System**

  

**1. Create Database**

```
CREATE DATABASE company_advanced;
USE company_advanced;
```

**2. Create Tables**

```
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department_id INT,
    salary DECIMAL(10,2),
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

CREATE TABLE departments (
    id INT PRIMARY KEY,
    name VARCHAR(50)
);
```

**3. Insert Sample Data**

```
INSERT INTO employees (id, name, department_id, salary)  
VALUES (1, 'Alice', 1, 60000),
       (2, 'Bob', 2, 75000);

INSERT INTO departments (id, name) VALUES (1, 'HR'), (2, 'Engineering');
```

**4. Query Data**

```
SELECT employees.name, employees.salary, departments.name AS department  
FROM employees  
JOIN departments ON employees.department_id = departments.id;
```

  

---

**Conclusion**

  

Now you’ve mastered **advanced SQL**, including:

• **Transactions & ACID**

• **Stored Procedures, Views, Triggers**

• **Advanced Joins, Window Functions, CTEs**

• **User Permissions & Indexing**

• **SQL vs. NoSQL concepts**

  

With this knowledge, you’re ready to build **high-performance databases, optimize queries, and work on real-world applications.** 🚀

  

🔹 **Next Step:** Learn **SQL Lesson 3** (Big Data, Cloud Databases, and Performance Tuning).