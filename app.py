import streamlit as st

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


st.title("Hello, World!")

x = np.array([1,2,3,4,5,6,7,8,9])
y = x ** 2

#st.write(x)
#st.write(y)


df = pd.DataFrame([x,y]).T
df.columns = ['x','y']


st.write(df)


my_plot = sns.scatterplot(x=x, y=y)

st.pyplot(my_plot.figure)

