# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 23:48:10 2023

@author: Lenovo
"""


import pandas as pd

df=pd.read_csv('transaction.csv',sep=';')
df.info()

##mathematical operation on Tableau

df['ProfitPerItem'] = df['SellingPricePerItem'] - df['CostPerItem']

df['ProfitPerTransaction'] = df['NumberOfItemsPurchased'] * df['ProfitPerItem']
df['CostPerTransaction'] = df['NumberOfItemsPurchased'] * df['CostPerItem']
df['SalesPerTransaction'] = df['NumberOfItemsPurchased'] * df['SellingPricePerItem']


###profit calculation = sales-cost
df['ProfitPerTransaction'] = df['SalesPerTransaction'] - df['CostPerTransaction']

df['Markup'] = round(df['ProfitPerTransaction'] / df['CostPerTransaction'],2)


print(df['Day'].dtype)
my_date=df['Day'].astype(str)+'-'+df['Month']+'-'+df['Year'].astype(str)
df['date'] =my_date


##using iloc to view specific columns/view

df.iloc[:]

##using split keyword to split the client coluumn data
split_col=df['ClientKeywords'].str.split(',',expand=True)

##creating a new column for clients keyword column
df['ClientAge']=split_col[0]
df['ClientType']=split_col[1]
df['LengthOfContract']=split_col[2]

##using the replace function
df['ClientAge']=df['ClientAge'].str.replace('[' , '')
#df['ClientType'] = df['ClientType'].str.replace('[' , '')
df['LengthOfContract']=df['LengthOfContract'].str.replace(']' , '')


####using the lower function to change item in lowercase
df['ItemDescription']= df['ItemDescription'].str.lower()

###merging two files or two dataframes
####
seasons=pd.read_csv('value_inc_seasons.csv',sep=';')

###merging files merge_df = pd.merge(df_old , df_new , on='key' , how='')

df= pd.merge(df , seasons , on='Month')

###dropping columns
df = df.drop(['Year' , 'Month' , 'Day'] ,axis=1)    
df = df.drop('ClientKeywords' ,axis=1) 

###export into csv
df.to_csv('ValueInc_Cleaned.csv', index=False)















