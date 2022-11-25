# What is natural join?
A NATURAL JOIN is a JOIN operation that creates an implicit join clause for us based on the common columns in the two tables being joined. Common columns are columns that have the same name in both tables. A NATURAL JOIN can be an INNER join, a LEFT OUTER join, or a RIGHT OUTER join. The default is INNER join

# write a query to join two columns by natural join
```sql
SELECT * 
FROM company.branch,company.client
where branch.branch_id = client.branch_id;
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/203887057-441ba8c8-4d67-435b-aad6-3354d5fcdcc9.png)

# write a query to inner join two columns by natural join
```sql
SELECT branch_name,client_name 
FROM company.branch
JOIN company.client
ON branch.branch_id = client.branch_id;
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/203888564-32a21a2e-001a-4250-956e-1c73ec9b9819.png)


# write a query to count the number of rows 
```sql
SELECT count(*) as "Number of Branches" 
FROM company.branch;
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/203889992-3d2687c6-de3d-4379-b630-bc1ac4d8f40d.png)


# write a group by query   
```sql
SELECT supplier_name,supply_type,count(*) 
FROM company.branch_supplier
group by supply_type;
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/203891634-20e612d4-5be8-49f4-828a-d8318abf6c6f.png)


# write a query to create new table and insert fetch data    
```sql
create table account
(
supplier_name varchar(50) not null,
supply_type varchar(50) not null,
primary key(supplier_name)
);

insert into account
SELECT supplier_name,supply_type
FROM company.branch_supplier
group by supply_type;
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/203907323-4a712915-f628-4436-8957-c65961b88ed1.png)


# write a query to create view table    
```sql
create view details as
SELECT supplier_name,supply_type,count(*) 
FROM company.branch_supplier
group by supply_type;
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/203907809-e1463330-0580-4679-ba89-ea30b111eb9d.png)


# write a query to create csv file and store data from tables    
```sql
FROM company.branch
into outfile 'd:\\branch.csv'
fields enclosed by '"' terminated by ',' escaped by '\\'
lines terminated by '\r\n';
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/203921096-5c3b3645-13fc-4594-b3f3-bb19cafd0338.png)



# write a query to load csv file data and store into tables    
## write query to delete records first and then insert
```sql
delete
from branch
where branch_id>0;
```

```sql
load data
infile 'd:\\branch.csv'
into table company.branch
fields enclosed by '"' terminated by ',' escaped by '\\'
lines terminated by '\r\n';

select *
from branch;
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/203922791-fb83b8c9-e186-4331-a802-b18157f684b8.png)

![image](https://user-images.githubusercontent.com/80588277/203922877-bacfc7fa-6a60-4469-b97c-8c36292fe228.png)


# write a query to create new table    
```sql
create table new_table
like company.employee;

insert new_table
select *
from employee
where emp_id < 106;
```

## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/203947744-2c536c46-0bef-47e2-8033-63836ab92cfb.png)


# write a query to update a record    
```sql
update company.employee
set salary = 5000000
where emp_id = 100;


select *
from company.employee;
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/203954121-23e89c29-6280-41d9-8717-e2974eec0973.png)

![image](https://user-images.githubusercontent.com/80588277/203954186-349f58d9-e35f-4960-80a4-e12c7a49a3ec.png)

