import streamlit as st
import pandas as pd

st.title('NFL Game Stats Analysis')

offK = pd.read_csv('nfl_package/datasets/kc_offensive_game_stats_cleaned.csv')
defK = pd.read_csv('nfl_package/datasets/kc_opp_game_stats_cleaned.csv')
offM = pd.read_csv('nfl_package/datasets/min_offensive_game_stats_cleaned.csv')
defM = pd.read_csv('nfl_package/datasets/min_opp_game_stats_cleaned.csv')

offK['team'] = 'Kansas City'
offM['team'] = 'Minnesota'

offense = pd.concat([offK, offM], ignore_index=True)
offense.reset_index(drop=True, inplace=True)

defense = pd.concat([defK, defM], ignore_index=True)
defense.reset_index(drop=True, inplace=True)

st.sidebar.header("Filter Data Here")

team = st.sidebar.selectbox("Select Team", ["All", "Kansas City", "Minnesota"])

win_loss = st.sidebar.selectbox("Select Win/Loss", ["All", "W", "L"])

year = st.sidebar.slider("Select Year", int(offense['year'].min()), int(offense['year'].max()), (2019, 2023))

if team != "All":
    offense = offense[offense['team'] == team]
    defense = defense[defense['team'] == team]

if win_loss != "All":
    offense = offense[offense['win_loss'] == win_loss]
    defense = defense[defense['win_loss'] == win_loss]

offense = offense[(offense['year'] >= year[0]) & (offense['year'] <= year[1])]
defense = defense[(defense['year'] >= year[0]) & (defense['year'] <= year[1])]


tab1, tab2 = st.tabs(["Offense", "Defense"])

with tab1:
    st.write(offense)

with tab2:
    st.write(defense)
