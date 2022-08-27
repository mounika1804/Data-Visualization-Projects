##https://www.kaggle.com/code/aremoto/retail-sales-forecast/notebook

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import zipfile
#zip_file = zipfile.ZipFile('retail-data-analytics.zip','r')
#zip_file.namelist()

features=pd.read_csv(r"C:\\Users\mouni\OneDrive\Desktop\pythonProject\Project 3\Features data set.csv")
sales=pd.read_csv(r"C:\\Users\mouni\OneDrive\Desktop\pythonProject\Project 3\sales data-set.csv")
stores=pd.read_csv(r"C:\\Users\mouni\OneDrive\Desktop\pythonProject\Project 3\stores data-set.csv")

features['Date']=pd.to_datetime(features['Date'])
sales['Date']=pd.to_datetime(sales['Date'])

print(features.shape)
print(sales.shape)
print(stores.shape)

print(sales[0:1].Date,sales[-1:].Date)
print(features[0:1].Date,features[-1:].Date)

df=pd.merge(sales,features,on=['Store','Date','IsHoliday'],how='left')
df=pd.merge(df,stores,on=['Store'],how='left')

df=df.fillna(0)
df['Temperature']=(df['Temperature']-32)*5./9.

types_encoded,types=df['Type'].factorize()
df['Type']=types_encoded
print(df.head())
print('training_data duplicated:{}'.format(df.duplicated().sum()))
df.drop_duplicates(inplace=True)

print(df.describe())

tab_info=pd.DataFrame(df.dtypes).T.rename(index={0:'column Type'})
tab_info=tab_info.append(pd.DataFrame(df.isnull().sum()).T.rename(index={0:'null values(nb'}))
tab_info=tab_info.append(pd.DataFrame(df.isnull().sum()/df.shape[0]*100).T.rename(index={0:'null values(%)'}))
print(tab_info)

df[['Date','Temperature','Fuel_Price','CPI','Unemployment','MarkDown1','MarkDown2','MarkDown3','MarkDown4','MarkDown5']].plot(x='Date',subplots=True,figsize=(20,15))
#plt.show()

df_average_sales_week=df.groupby(by=['Date'],as_index=False)['Weekly_Sales'].sum()
df_average_sales=df_average_sales_week.sort_values('Weekly_Sales',ascending=False)

plt.figure(figsize=(20,15))
plt.plot(df_average_sales_week.Date,df_average_sales_week.Weekly_Sales)
#plt.show()

print(df_average_sales.head())

print(df_average_sales[::-1].head())

ts=df_average_sales_week.set_index('Date')
#ts=ts.resample('H').ffill()
#ts=ts.resample('W").sum()
print(df_average_sales[::-1].head())

df_top_stores=df.groupby(by=['Type'],as_index=False)['Weekly_Sales'].sum()
print(df_top_stores.sort_values('Weekly_Sales',ascending=False))

df_top_stores=df.groupby(by=['Store'],as_index=False)['Weekly_Sales'].sum()
print(df_top_stores.sort_values('Weekly_Sales',ascending=False)[:3])
