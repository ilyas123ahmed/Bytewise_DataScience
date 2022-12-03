
import glassdoor_scraper as gs
import pandas as pd
path = "D:/Bytewise_Internship/Salary_Project/chromedriver"

df = gs.get_jobs("data scientist", 15,False,path, 15)
df.to_csv('new.csv', index=False)