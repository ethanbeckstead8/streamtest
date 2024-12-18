import streamlit as st
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title('hello')
st.write('hi')
offK = pd.read_csv('nfl_package/datasets/kc_offensive_game_stats_cleaned.csv')
defK = pd.read_csv('nfl_package/datasets/kc_opp_game_stats_cleaned.csv')
offM = pd.read_csv('nfl_package/datasets/min_offensive_game_stats_cleaned.csv')
offD = pd.read_csv('nfl_package/datasets/min_opp_game_stats_cleaned.csv')
st.sidebar.header("Filter Data Here")
tab1, tab2 = st.tabs(["Offense", "Defense"])
