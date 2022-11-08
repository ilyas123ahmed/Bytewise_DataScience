# write a query to create a schema in SQL
create database student;

## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200487867-9fd0dbb3-4cf6-43bd-9342-c885a6774ae2.png)


# write a query to create a table in specific schema
use student;
create table students (
  student_id INT,
  name varchar(20),
  major varchar(20),
  primary key(student_id)
);


# write a query to describe a table 
describe students;
