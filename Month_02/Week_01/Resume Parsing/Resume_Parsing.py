#!/usr/bin/env python
# coding: utf-8

# ## Importing Libraries 

# In[6]:


import spacy
import pdfminer
import re
import os
import pandas as pd
import pdf2txt


# ## Load the Language Model

# In[7]:


nlp = spacy.load("en_core_web_sm")


# ## Making a function to read pdf files(converting pdf to text file)

# In[8]:


def convert_pdf(f):
    output_filename = os.path.basename(os.path.splitext(f)[0]) + ".txt"
    output_filepath = os.path.join("output/txt/", output_filename)
    pdf2txt.main(args=[f, "--outfile", output_filepath])
    print(output_filepath + " saved successfully!!!")
    return open(output_filepath).read()


# In[9]:


result_dict = {'name': [], 'phone': [], 'email': [], 'skills': []} 
names = []
phones = []
emails = []
skills = []


# ## Extracting all the pdf text data

# In[10]:


def parse_content(text):
    skillset = re.compile("python|java|sql|hadoop|tableau")
    phone_num = re.compile(
        "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
    )
    doc = nlp(text)
    name = [entity.text for entity in doc.ents if entity.label_ == "PERSON"][0]
    print(name)
    email = [word for word in doc if word.like_email == True][0]
    print(email)
    phone = str(re.findall(phone_num, text.lower()))
    skills_list = re.findall(skillset, text.lower())
    unique_skills_list = str(set(skills_list))
    names.append(name)
    emails.append(email)
    phones.append(phone)
    skills.append(unique_skills_list)
    print("Extraction completed successfully!!!")


# ## Creating and writing the scraped data from pdf

# In[11]:


for file in os.listdir('resumes/'):
    if file.endswith('.pdf'):
        print('Reading.....' + file)
        txt = convert_pdf(os.path.join('resumes/',file))
        parse_content(txt)


# In[12]:


names


# In[13]:


phones


# In[14]:


emails


# In[15]:


skills


# ## Creating Dataframes

# In[16]:


result_dict['name'] = names
result_dict['phone'] = phones
result_dict['email'] = emails
result_dict['skills'] = skills


# In[19]:


result_dict


# In[20]:


result_df = pd.DataFrame(result_dict)
result_df


# In[ ]:


# Creating a CSV file
result_df.to_csv("Parsed_Data.csv")


# In[ ]:


# Reading created CSV file


# In[ ]:


df = pd.read_csv("Parsed_Data.csv")
df

