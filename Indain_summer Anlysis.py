import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ['City', 'Date', 'tempmax', 'tempmin', 'temp', 'feelslikemax',
#        'feelslikemin', 'feelslike', 'dew', 'humidity', 'windspeed', 'winddir',
#        'sealevelpressure', 'cloudcover', 'visibility', 'sunrise', 'sunset',
#        'moonphase', 'conditions', 'description']

df = pd.read_csv('Indian Summers - Over the years.csv')
# print(df.head(9))
# print(df.tail(9))
# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())
# df=df.drop(['sealevelpressure'],axis=1)  # axis= 1 means function is applied row wise on the df.

# print(df.columns)
# df.dropna(inplace=True)
# print(df.shape)
# print(df['conditions'].unique())
# print(df['conditions'].value_counts())
# plt.figure(figsize=(11,4))  # figsize define the length and width of fig frame.
# sns.countplot('conditions',data=df,palette='hls')
# plt.xticks(rotation=90)  # rotation shift the text by degree on x or y-axis.
# plt.show()

# count_clear=len(df.loc[df['conditions']=='Clear'])
# per_clear=(count_clear/len(df.conditions)*100)
# print(per_clear)

# a=df[['humidity','tempmax','tempmin','windspeed']].describe()
# print(a)

# HISTOGRAM PLOT:

sns.set(style='darkgrid')
sns.histplot(x='humidity',data=df,kde=True)  # ax define in which graph you want fig.
plt.show()

# VIOLIN PLOT:
# fig,axs=plt.subplots(2,2,figsize=(10,8))# subplot define no of graphs wants in row & column.
# sns.set(style='darkgrid')
# sns.violinplot(x='humidity',data=df,ax=axs[1,0])  # kde Kernel Density Estimation (KDE) is a way to estimate
# plt.show()                                         # the probability density function of a continuous random variable.

# BOX PLOT:
plt.figure(figsize=(10,6))
sns.boxplot('humidity','conditions',data=df)
plt.show()

# # HEATMAP PLOT:
# plt.figure(figsize=(12, 14))
# sns.heatmap(df.corr(), annot=True, cmap='coolwarm')  # annot is used in heatmap to see numeric value in graph.
# plt.show()                                           # cmap used to customize colour in heatmap.
