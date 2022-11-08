# Write a query to create a table called Employee
```sql
CREATE TABLE employee (
  emp_id INT PRIMARY KEY,
  first_name VARCHAR(40),
  last_name VARCHAR(40),
  birth_day DATE,
  sex VARCHAR(1),
  salary INT,
  super_id INT,
  branch_id INT
);
```

# Write a query to create a table called Branch
```sql
CREATE TABLE branch (
  branch_id INT PRIMARY KEY,
  branch_name VARCHAR(40),
  mgr_id INT,
  mgr_start_date DATE,
  FOREIGN KEY(mgr_id) REFERENCES employee(emp_id) ON DELETE SET NULL
);
```

# Write a query to perfrom alteration on a table called Employee
```sql
ALTER TABLE employee
ADD FOREIGN KEY(branch_id)
REFERENCES branch(branch_id)
ON DELETE SET NULL;

ALTER TABLE employee
ADD FOREIGN KEY(super_id)
REFERENCES employee(emp_id)
ON DELETE SET NULL;
```


# Write a query to create a table called Client
```sql
CREATE TABLE client (
  client_id INT PRIMARY KEY,
  client_name VARCHAR(40),
  branch_id INT,
  FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE SET NULL
);
```

# Write a query to create a table called Works_with
```sql
CREATE TABLE works_with (
  emp_id INT,
  client_id INT,
  total_sales INT,
  PRIMARY KEY(emp_id, client_id),
  FOREIGN KEY(emp_id) REFERENCES employee(emp_id) ON DELETE CASCADE,
  FOREIGN KEY(client_id) REFERENCES client(client_id) ON DELETE CASCADE
);
```

# Write a query to create a table called Branch Supplier
```sql
CREATE TABLE branch_supplier (
  branch_id INT,
  supplier_name VARCHAR(40),
  supply_type VARCHAR(40),
  PRIMARY KEY(branch_id, supplier_name),
  FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE CASCADE
);
```


-- Corporate
# Write a query to insert values in a table 
```sql
INSERT INTO employee VALUES(100, 'David', 'Wallace', '1967-11-17', 'M', 250000, NULL, NULL);

INSERT INTO branch VALUES(1, 'Corporate', 100, '2006-02-09');

UPDATE employee
SET branch_id = 1
WHERE emp_id = 100;

INSERT INTO employee VALUES(101, 'Jan', 'Levinson', '1961-05-11', 'F', 110000, 100, 1);

-- Scranton
INSERT INTO employee VALUES(102, 'Michael', 'Scott', '1964-03-15', 'M', 75000, 100, NULL);

INSERT INTO branch VALUES(2, 'Scranton', 102, '1992-04-06');

UPDATE employee
SET branch_id = 2
WHERE emp_id = 102;

INSERT INTO employee VALUES(103, 'Angela', 'Martin', '1971-06-25', 'F', 63000, 102, 2);
INSERT INTO employee VALUES(104, 'Kelly', 'Kapoor', '1980-02-05', 'F', 55000, 102, 2);
INSERT INTO employee VALUES(105, 'Stanley', 'Hudson', '1958-02-19', 'M', 69000, 102, 2);

-- Stamford
INSERT INTO employee VALUES(106, 'Josh', 'Porter', '1969-09-05', 'M', 78000, 100, NULL);

INSERT INTO branch VALUES(3, 'Stamford', 106, '1998-02-13');

UPDATE employee
SET branch_id = 3
WHERE emp_id = 106;

INSERT INTO employee VALUES(107, 'Andy', 'Bernard', '1973-07-22', 'M', 65000, 106, 3);
INSERT INTO employee VALUES(108, 'Jim', 'Halpert', '1978-10-01', 'M', 71000, 106, 3);


-- BRANCH SUPPLIER
INSERT INTO branch_supplier VALUES(2, 'Hammer Mill', 'Paper');
INSERT INTO branch_supplier VALUES(2, 'Uni-ball', 'Writing Utensils');
INSERT INTO branch_supplier VALUES(3, 'Patriot Paper', 'Paper');
INSERT INTO branch_supplier VALUES(2, 'J.T. Forms & Labels', 'Custom Forms');
INSERT INTO branch_supplier VALUES(3, 'Uni-ball', 'Writing Utensils');
INSERT INTO branch_supplier VALUES(3, 'Stamford Lables', 'Custom Forms');
INSERT INTO branch_supplier VALUES(3, 'Hammer Mill', 'Paper');

-- CLIENT
INSERT INTO client VALUES(400, 'Dunmore Highschool', 2);
INSERT INTO client VALUES(401, 'Lackawana Country', 2);
INSERT INTO client VALUES(402, 'FedEx', 3);
INSERT INTO client VALUES(403, 'John Daly Law, LLC', 3);
INSERT INTO client VALUES(404, 'Scranton Whitepages', 2);
INSERT INTO client VALUES(405, 'Times Newspaper', 3);
INSERT INTO client VALUES(406, 'FedEx', 2);

-- WORKS_WITH
INSERT INTO works_with VALUES(105, 400, 55000);
INSERT INTO works_with VALUES(102, 401, 267000);
INSERT INTO works_with VALUES(108, 402, 22500);
INSERT INTO works_with VALUES(107, 403, 5000);
INSERT INTO works_with VALUES(108, 403, 12000);
INSERT INTO works_with VALUES(105, 404, 33000);
INSERT INTO works_with VALUES(107, 405, 26000);
INSERT INTO works_with VALUES(102, 406, 15000);
INSERT INTO works_with VALUES(105, 406, 130000);
```


# Write a query to find all Employees
```sql
select * 
from employee;
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200556111-41702a74-cd00-4802-8c20-b22bd541dc27.png)


# Write a query to find all Clients
```sql
select * 
from client;
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200556456-90dd6174-c76a-4dd7-8707-48e8c37ef344.png)



# Write a query to find all employees order by salary
```sql
select * 
from employee
order by salary;
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200556808-d5358239-aa8e-4a28-ba62-fc7d9ddf8f95.png)


# Write a query to find all employees order by sex  and then by name
```sql
select * 
from employee
order by sex,first_name,last_name;
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200557266-ecedd598-f378-4c60-9572-914ce15c765e.png)


# Write a query to find first 5 employees
```sql
select * 
from employee
limit 5;
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200557975-67bb0371-99f9-48bc-ac30-1ef49b44936c.png)


# Write a query to find first and last name of employees
```sql
select first_name,last_name
from employee;
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200558407-f3d7e35e-0d37-463e-9080-aea1d000dc17.png)


# Write a query to change the name of column
```sql
select first_name AS forname,last_name as sirname
from employee;
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200558954-7b532008-3538-43b7-ae7e-5457a518e0ff.png)


# Write a query to find all different genders
```sql
select distinct sex
from employee;
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200559347-587e42a2-3d4d-4c11-82d8-7d44d02b9ec1.png)


# Write a query to find the number of employees
```sql
select count(emp_id)
from employee;
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200564365-51c7b983-5d57-4837-adfd-05c0723ead0e.png)


# Write a query to find the average of all the employee's salary
```sql
select AVG(salary)
from employee;
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200565863-12b2262a-225d-4d0f-961d-d6a1fd2b5703.png)


# Write a query to find the sum of all the employee's salary
```sql
select sum(salary)
from employee;
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200566816-5e08be59-e309-4d12-9221-a87482194339.png)


# Write a query to find the count the number of male and female
```sql
select count(sex),sex
from employee
group by sex;
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200567591-e488ccee-a368-468c-9927-f03e5db31c4c.png)


# Write a query to find a client who are an LLC
```sql
select *
from client
WHERE client_name like '%LLC';
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200570478-fb936394-cc7b-4a30-859d-994efe227e63.png)


# Write a query to find any emplyee who born in october
```sql
select *
from employee
WHERE birth_day like '____-10%';
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200573078-7a0ed1d4-6e13-41cc-b993-375501692651.png)


# Write a query to find the list of emplyee and branch names
```sql
select first_name
from employee
union
select branch_name
from branch;
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200574125-3cf19ecb-3c48-4517-ae86-61ec27e2f48c.png)


# Write a query to implement join 
```sql
-- Add the extra branch
INSERT INTO branch VALUES(4, "Buffalo", NULL, NULL);

SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
JOIN branch    -- LEFT JOIN, RIGHT JOIN
ON employee.emp_id = branch.mgr_id;
```

## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200582503-06fb02d0-88be-4e5d-9c79-2878d3eaaf3b.png)



# Write a query to find names of all employees who have sold over 50,000 
```sql
SELECT employee.first_name, employee.last_name
FROM employee
WHERE employee.emp_id IN (SELECT works_with.emp_id
                          FROM works_with
                          WHERE works_with.total_sales > 50000);

```

## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200585941-915d0f03-fd9e-48d8-92da-6d3c5abfbb95.png)

