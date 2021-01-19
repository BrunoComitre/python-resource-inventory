import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier


st.write("""
# Simple Iris Flower Prediction App
This app predicts the **Iris Flower** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_lenght = st.sidebar.slider('Sepal lenght', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_lenght = st.sidebar.slider('Petal lenght', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal widht', 0.1, 2.5, 0.2)
    data = {'sepal_lenght': sepal_lenght,
            'sepal_width': sepal_width,
            'petal_lenght': petal_lenght,
            'petal_widht': petal_width
           }
    features = pd.DataFrame(data, index=[0])
    return features

dataframe = user_input_features()

st.subheader('User Input Parameters')
st.write(dataframe)

iris = datasets.load_iris()
X = iris.data
Y = iris.target

classifier = RandomForestClassifier()
classifier.fit(X, Y)

prediction = classifier.predict(dataframe)
prediction_proba = classifier.predict_proba(dataframe)

st.subheader('Class labels and theis corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])
# st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)

# print(prediction_proba)
