import sys
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import requests
import json

st.title('Covid-19 Global Cases')
st.write("It show ***Cornavirus Cases*** around the world")
st.sidebar.title("Selector")
st.markdown('<styyle>body{background-color: lightblue;}</style>',unsafe_allow_html=True)

print(sys.path)
print('Hello dashboard!')
#Loading the data
#response
