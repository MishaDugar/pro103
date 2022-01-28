import pandas as pd 
import plotly.express as px 

df=pd.read_csv("data1031.csv")
fig=px.scatter(df,x="date",y="cases",color="country") 
fig.show()