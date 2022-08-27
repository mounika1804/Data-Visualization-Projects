# https://www.kaggle.com/code/lakshitjain25/dummy-marketing-data-eda-ml

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
link="C:\\Users\\mouni\\Downloads\\archive\\Dummy Data HSS.csv"
df_orig=pd.read_csv(link)
print(df_orig)
df=df_orig.copy()
df=df.dropna()
print(df)
print(df.describe())
print(df.info())
print(df.Influencer.value_counts())        #print(df['Influencer'].value_counts()) -->we can write like this also
print(df.Influencer.unique())
df["Influencer_encoded"]=df["Influencer"]
influencer_mapping={'Mega':3,'Micro':1,'Nano':0,'Macro':2}
df["Influencer_encoded"]=df["Influencer_encoded"].map(influencer_mapping)
print(df.head())
col_names=['Macro','Mega','Micro','Nano']
print(df.groupby("Influencer")["Sales"].mean())
p=np.array(df.groupby("Influencer")["Sales"].mean())
print(p)
Influencer_df=pd.DataFrame()
Influencer_df["Type"]=col_names
Influencer_df["Value"]=p
print(Influencer_df)
sns.barplot(x=Influencer_df["Type"],y=Influencer_df["Value"])
plt.show()
sns.scatterplot(x=df["TV"],y=df["Sales"],cmap="rainbow")
plt.show()
sns.scatterplot(x=df["Radio"],y=df["Sales"],cmap="rainbow")
plt.show()
sns.scatterplot(x=df["Social Media"],y=df["Sales"])
plt.show()
sns.scatterplot(x=df["Social Media"],y=df["Sales"],cmap="rainbow",c=df["Influencer_encoded"])
plt.show()
sns.scatterplot(x=df["Influencer"],y=df["Social Media"],cmap="rainbow",c=df["Influencer_encoded"])
plt.show()
print(df.groupby("Influencer")["Social Media"].mean())




