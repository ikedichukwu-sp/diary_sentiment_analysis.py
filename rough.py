import glob
import streamlit as st
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer
directory = sorted(glob.glob(r"diary\*.txt"))
analyzer = SentimentIntensityAnalyzer()


negativity = []
positivity = []
date = []
for i in directory:
    with open(i) as file:
        content = file.read()
        scores = analyzer.polarity_scores(content)
        negativity.append(scores["neg"])
        positivity.append(scores["pos"])
        date.append(i.strip("diary\\").strip(".txt"))

st.header("Dairy tone")
st.subheader("positivity")

pos_figure = px.line(x=date, y=positivity, labels={"x": "date", "y": "positivity"})
st.plotly_chart(pos_figure)


st.subheader("negativity")
pos_figure = px.line(x=date, y=negativity, labels={"x": "date", "y": "positivity"})
st.plotly_chart(pos_figure)
print(date)
print(scores)
print(negativity)
print(positivity)
