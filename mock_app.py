import streamlit as st
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

st.title("Hello, World!")
st.text("This is an update to my file")



x = np.array([1,2,3,4,5,6,7,8,9])
y = x**2

df = pd.DataFrame([x,y]).T
df.columns = ['x','y']
df

my_fig = sns.scatterplot(x=x,y=y)

st.pyplot(my_fig.figure)