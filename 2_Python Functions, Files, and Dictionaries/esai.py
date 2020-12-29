import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Project 1-Sentiment Classifier.csv")
fig,ax=plt.subplots()
my_scatter_plot=ax.scatter(df[" Net Score"],df["Number of Retweets"])
plt.show()