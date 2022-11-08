# write a query to create a schema in SQL
```sql
create database student;
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200487867-9fd0dbb3-4cf6-43bd-9342-c885a6774ae2.png)


# write a query to create a table in specific schema
```sql
use student;
create table students (
  student_id INT,
  name varchar(20),
  major varchar(20),
  primary key(student_id)
);
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200491380-07cc94e5-8380-43dd-8650-7a362e5a5899.png)


# write a query to describe a table 
```sql
describe students;
```

## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200491457-5b8fdbec-18ac-4346-8d71-0566e74b1d04.png)


# Write a query to delete table from schema
```sql
 DROP table students;
```
## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200487867-9fd0dbb3-4cf6-43bd-9342-c885a6774ae2.png)


# Write a query to alter a table
```sql
ALTER TABLE students add
(
  gpa decimal(3,2)
);
```

## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200494732-cf29491f-0bfe-4628-bd79-c155a3c0311b.png)


# Write a query to alter specific column
```sql
alter table students drop column gpa;
```

## OUTPUT
![image](https://user-images.githubusercontent.com/80588277/200495275-73f6416f-08ab-466c-b9f3-ebb4a7f0cf15.png)


# Write a query to insert values in table
```sql
select * from students;
insert into students (student_id, name ,major)
values
 (1, 'ILYAS','Data Science'),
 (2, 'Ahmad','Data Engineer'),
 (3, 'Asad','Biology'),
 (4, 'Arham','Math'),
 (5, 'Tabish','Social Science');
 ```
 
 ## OUTPUT
 ![image](https://user-images.githubusercontent.com/80588277/200499037-11196496-b291-460e-b715-69522b55b675.png)

