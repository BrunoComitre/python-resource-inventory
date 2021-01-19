import streamlit as st
import pandas as pd
import numpy as np 


st.title('Security Review')

dataframe = pd.read_csv('winequality.csv')

if st.checkbox('Show Dataframe'):
    st.write(dataframe)

st.write("""
***
""")

st.write("""
# Teste Markdown
## Teste Markdown
### Teste Markdown
#### Teste Markdown
##### Teste Markdown
""")

st.write("""
***
""")

axis = st.slider('x')
st.write(axis, 'ao quadrado é', axis * axis)

st.write("""
***
""")

# Reuse this data across runs!
read_and_cache_csv = st.cache(pd.read_csv)

BUCKET = "https://streamlit-self-driving.s3-us-west-2.amazonaws.com/"

data = read_and_cache_csv(BUCKET + "labels.csv.gz", nrows=1000)
desire_label = st.selectbox('Filter to:', ['car', 'truck'])
st.write(data[data.label == desire_label])
