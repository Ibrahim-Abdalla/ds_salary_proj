# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 10:33:50 2020

@author: ibrahim
"""

import pandas as pd
df = pd.read_csv('glassdoor_jobs.csv')

#salary parsing

#df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
#df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df =df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('k','').replace('CA$',''))

#minus_hour = minus_kd.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:', ''))

df['min_salary'] = minus_kd.apply(lambda x: int(x.split('-')[0]))
df['min_salary'].dtype
df['max_salary'] = minus_kd.apply(lambda x: int(x.split('-')[1]))

df['avg_salary'] = (df['min_salary']+df['max_salary'])/2

#company name text only

df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

#state field

#df['job_state'] = df['Location'].apply(lambda x: x.split(',')[0])
df.job_state.value_counts()
df.columns

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)


#age of company

df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2020-x)

#parsing of job description (python, etc.)

df['Job Description'][0]

#pythom
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python.value_counts()

#r_studio
df['r studio'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() else 0)
df['r studio'].value_counts()

#spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

#aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()


df.to_csv('salary_data_cleaned.csv', index = False)
