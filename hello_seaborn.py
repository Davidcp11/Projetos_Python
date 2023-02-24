import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
import os

#Load the data
fifa_filepath = 'input/fifa.csv'
#Read the file into a variable fifa_data
fifa_data = pd.read_csv(fifa_filepath, index_col='Date', parse_dates=True)
#Plot the data
plt.figure(figsize=(16, 6))
#Line chart showing how FIFA ranking evolved over time
sns.lineplot(data=fifa_data)
plt.show()
