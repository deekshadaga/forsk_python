# -*- coding: utf-8 -*-
"""pandas

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZDwaHC41gfjo-SEnDbZzx8d5FDi2lcGi
"""

import pandas as pd
import io
import matplotlib.pyplot as plt
from google.colab import files
uploaded = files.upload()
df = pd.read_csv(io.BytesIO(uploaded['Salaries.csv']))

#1. Which Male and Female Professor has the highest and the lowest salaries
d1=df[(df['sex']=='Male') & (df['rank']=='Prof')]
d2=df[(df['sex']=='Female') & (df['rank']=='Prof')]
print('For male professors :\nHighest salary is =',d1['salary'].max(),'\nLowest salary is =',d1['salary'].min())
print('For female professors :\nHighest salary is =',d2['salary'].max(),'\nLowest salary is =',d2['salary'].min())

#2. Which Professor takes the highest and lowest salaries.
d3=df[(df['rank']=='Prof')]
print('For professors :\nHighest salary is =',d3['salary'].max(),'\nLowest salary is =',d3['salary'].min())

#3. Missing Salaries - should be mean of the matching salaries of those whose service is the same

#4. Missing phd - should be mean of the matching service

#5. How many are Male Staff and how many are Female Staff. 

#Show both in numbers and Graphically using Pie Chart.  

print('number of staff :\n',df['sex'].value_counts(),'\n\nPie chart :')
df.sex.value_counts().plot.pie()
plt.show()

#Show both numbers and in percentage

print('number of staff :\n',df['sex'].value_counts(),'\n\nPercentage :\n',df['sex'].value_counts(normalize=True)*100)

#6. How many are Prof, AssocProf and AsstProf. Show both in numbers adn Graphically using a Pie Chart
print('number of staff :\n',df['rank'].value_counts(),'\n\nPie chart :')
df['rank'].value_counts().plot.pie()
plt.show()

#7. Who are the senior and junior most employees in the organization.

#8. Draw a histogram of the salaries divided into bin starting from 50K and increment of 15K