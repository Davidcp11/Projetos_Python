import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

# save filepath to variable for easier access
agricultural_file = 'input/agricultural_raw_material.csv'
# read the data and store data in DataFrame titled melbourne_data
df = pd.read_csv(agricultural_file)
# Checking Null values
print (df.isnull().sum())
# Replacing %,"-" and ","
df = df.replace('%', '', regex=True)
df = df.replace(',', '', regex=True)
df = df.replace('-', '', regex=True)
df = df.replace('', np.nan)
# Dropping rows with NaN values
df = df.dropna()
# Checking Null values
print (df.isnull().sum())

lst = ["Coarse wool Price",
       "Coarse wool price % Change",
       "Copra Price",
       "Copra price % Change",
       "Cotton Price",
       "Cotton price % Change",
       "Fine wool Price",
       "Fine wool price % Change",
       "Hard log Price",
       "Hard log price % Change",
       "Hard sawnwood Price",
       "Hard sawnwood price % Change",
       "Hide Price",
       "Hide price % change",
       "Plywood Price",
       "Plywood price % Change",
       "Rubber Price",
       "Rubber price % Change",
       "Softlog Price",
       "Softlog price % Change",
       "Soft sawnwood Price",
       "Soft sawnwood price % Change",
       "Wood pulp Price",
       "Wood pulp price % Change"]
df[lst] = df[lst].astype("float")
df.Month = pd.to_datetime(df.Month.str.upper(), format="%b%y", yearfirst=False)
df = df.set_index('Month')


sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 12
matplotlib.rcParams['figure.figsize'] = (12, 9)
matplotlib.rcParams['figure.facecolor'] = '#00000000'
#raw-materials list
raw_data = ["Coarse wool Price",
            "Copra Price",
            "Cotton Price",
            "Fine wool Price",
            "Hard log Price",
            "Hard sawnwood Price",
            "Hide Price",
            "Plywood Price",
            "Rubber Price",
            "Softlog Price",
            "Soft sawnwood Price",
            "Wood pulp Price"]
#correlation
corrmat = df[raw_data].corr()
#fig size
fig = plt.figure(figsize=(15, 15))
#grafic
mask = np.triu(np.ones_like(corrmat, dtype=bool))
sns.heatmap(corrmat, vmax= .8, mask=mask, square=True, annot=True)
plt.show()
#price and change
axes = df[["Coarse wool Price", "Coarse wool price % Change"]].plot(figsize=(11, 9),subplots=True, linewidth=1)
plt.show()
#Change price
change_list = ["Coarse wool price % Change",
       "Copra price % Change",
       "Cotton price % Change",
       "Fine wool price % Change",
       "Hard log price % Change",
       "Hard sawnwood price % Change",
       "Hide price % change",
       "Plywood price % Change",
       "Rubber price % Change",
       "Softlog price % Change",
       "Soft sawnwood price % Change",
       "Wood pulp price % Change"]
for i in range(len(change_list)):
       plt.figure(figsize=(12, 12))
       df[change_list[i]].hist(figsize=(8, 6), linewidth=1)
       plt.xlabel('%Change')
       plt.ylabel('Count')
       plt.legend(change_list[i:], loc='upper center', bbox_to_anchor=(0.5, 1))
       plt.show()
for i in range(len(raw_data)):
       plt.subplot(4, 3, i+1)
       plt.subplots_adjust(hspace=1, wspace=0.5)
       plt.title(raw_data[i])
       plt.plot(df[raw_data[i]])
       plt.xticks(rotation=90)
plt.show()
# Cotton and Rubber
plt.figure(figsize=(10, 10))
plt.plot(df[["Cotton Price", "Rubber Price"]])
plt.title("Materials Price Comparision")
plt.xlabel('Years')
plt.ylabel('Prices')
plt.legend(['Cotton Price', 'Rubber Price'], loc='upper center',bbox_to_anchor=(0.5, 1))
plt.show()
