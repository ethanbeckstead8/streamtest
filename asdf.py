import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title('hello')
st.write('hi')
offK = pd.read_csv('nfl_package/datasets/kc_offensive_game_stats_cleaned.csv')
defK = pd.read_csv('nfl_package/datasets/kc_opp_game_stats_cleaned.csv')
offM = pd.read_csv('nfl_package/datasets/min_offensive_game_stats_cleaned.csv')
offD = pd.read_csv('nfl_package/datasets/min_opp_game_stats_cleaned.csv')
offK['team'] = 'Kansas City'
offM['team'] = 'Minnesota'

offense = pd.concat([offK, offM], ignore_index=True)
offense.reset_index(drop=True, inplace=True)
defense = pd.concat([defK, defM], ignore_index=True)
defense.reset_index(drop=True, inplace=True)
st.sidebar.header("Filter Data Here")
tab1, tab2 = st.tabs(["Offense", "Defense"])
with tab1:
  st.write(offense)
with tab2:
  st.write(defense)
