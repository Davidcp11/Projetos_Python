import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
import os

#Read the data
spotify_filepath = 'input/spotify.csv'
spoify_data = pd.read_csv(spotify_filepath, index_col='Date', parse_dates=True)
#Plot the data
plt.figure(figsize=(14, 6))
plt.title("Daily Global Streams of Popular Songs in 2017-2018")
sns.lineplot(data=spoify_data['Despacito'], label='Despacito')
sns.lineplot(data=spoify_data['Shape of You'], label='Shape of You')
plt.show()