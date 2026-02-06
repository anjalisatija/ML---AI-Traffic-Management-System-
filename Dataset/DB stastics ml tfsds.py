import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_excel('C:\\Users\\Asus\\Downloads\\ML AI TMS\\traffic_data_1.xlsx')

# Statistical Analysis for our dataset-
mean_values = df.mean(numeric_only=True)
variance_values = df.var(numeric_only=True)
median_values = df.median(numeric_only=True)
mode_values = df.mode(numeric_only=True).iloc[0]

print("Mean Values:\n", mean_values)
print("Variance Values:\n", variance_values)
print("Median Values:\n", median_values)
print("Mode Values:\n", mode_values)

sns.lineplot(x='time', y='pedestrian', data=df)
plt.title('Trend of Pedestrian Over Time')
plt.xlabel('Time')
plt.ylabel('Pedestrian Count')
plt.show()

sns.violinplot(x='timezone', y='bike', data=df)
plt.title('Distribution of Bike Counts by Timezone')
plt.xlabel('Timezone')
plt.ylabel('Bike Count')
plt.show()

sns.jointplot(x='carspeed00', y='carspeed10', data=df, kind='scatter', marginal_kws=dict(bins=25, fill=True))
plt.title('Relationship Between Carspeed00 and Carspeed10')
