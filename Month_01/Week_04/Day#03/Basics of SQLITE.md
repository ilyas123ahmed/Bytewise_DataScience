# Basics of SQLITE

```python
import sqlite3

conn = sqlite3.connect("myquotes.db")
curr = conn.cursor()
curr.execute("""create table quotes_tb(
            title text,
            author text,
            tag text
            )""")

# curr.execute("""insert into quotes_tb values('Python is awesome','buildwithpython','python')""")
conn.commit()
conn.close()
```
after runnning above program then we comment create table lines because we already create table.  

```python
import sqlite3

conn = sqlite3.connect("myquotes.db")
curr = conn.cursor()
# curr.execute("""create table quotes_tb(
#             title text,
#             author text,
#             tag text
#             )""")

curr.execute("""insert into quotes_tb values('Python is awesome','buildwithpython','python')""")
conn.commit()
conn.close()
```

### Output of database

![image](https://user-images.githubusercontent.com/80588277/192130089-0b0dff3b-a4cd-45b9-97a7-d8b980b2c0cc.png)

![image](https://user-images.githubusercontent.com/80588277/192130078-a560974b-5d03-49c5-b411-864ee52a3ec5.png)
