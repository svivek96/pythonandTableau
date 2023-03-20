# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 17:59:07 2023

@author: Lenovo
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_json('loan_data_json.json')

json_file =open('loan_data_json.json')
data = json.load(json_file)

#transform data to dataframe
loandata = pd.DataFrame(data)

##finding unique values for the purpose column
loandata['purpose'].unique()

##describe the data 
loandata.describe()

##describe the data for specific column 
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using EXP() to get the annual income
income =np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income


#fico score


ficocat=[]
for i in range(0,len(loandata)):
    category=loandata['fico'][i]
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 780:
            cat = 'Good'
        elif category >=780:
            cat = 'Excellent'
        else :
            cat ='Unknown'
    except:
        cat ='Unknown'        
    ficocat.append(cat)    
    
ficocat = pd.Series(ficocat)    

loandata['fico.category'] = ficocat

###df.loc as a conditional statement
#df.loc[df[columnname] condition, new columnname] = 'value' if the condition is met.
# for interest rates a new column is wanted, rate >0.12 then high else low.

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

#number of loans/rows by fico category
catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color='red',width=0.1)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color='green',width=0.5)
plt.show()


###scatter plots

ypoint=loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint,color='purple')
plt.show()


##writing to csv
loandata.to_csv('loan_cleaned.csv', index=True)
















    



