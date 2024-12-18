import streamlit as st
import pandas as pd

st.title('NFL Game Stats Analysis')

offK = pd.read_csv('nfl_package/datasets/kc_offensive_game_stats_cleaned.csv')
defK = pd.read_csv('nfl_package/datasets/kc_opp_game_stats_cleaned.csv')
offM = pd.read_csv('nfl_package/datasets/min_offensive_game_stats_cleaned.csv')
defM = pd.read_csv('nfl_package/datasets/min_opp_game_stats_cleaned.csv')

offK['team'] = 'Kansas City'
offM['team'] = 'Minnesota'
defM['team'] = 'Minnesota'
defK['team'] = 'Kansas City'

offense = pd.concat([offK, offM], ignore_index=True)
offense.reset_index(drop=True, inplace=True)

defense = pd.concat([defK, defM], ignore_index=True)
defense.reset_index(drop=True, inplace=True)

offense = offense[['team'] + [col for col in offense.columns if col != 'team']]
defense = defense[['team'] + [col for col in offense.columns if col != 'team']]


st.sidebar.header("Filter Data Here")

team = st.sidebar.selectbox("Team", ["All", "Kansas City", "Minnesota"])

win_loss = st.sidebar.selectbox("Game Outcome", ["All", "W", "L"])


home_or_away = st.sidebar.radio("Home or Away", ["All", "home", "away"])

year = st.sidebar.selectbox("Year", ["All"] + sorted(offense['year'].unique().tolist()))



filtered_offense = offense[
    ((offense['team'] == team) | (team == "All")) &
    ((offense['win_loss'] == win_loss) | (win_loss == "All")) &
    ((offense['home_or_away'] == home_or_away) | (home_or_away == "All")) &
    ((offense['year'] == year) | (year == "All"))
]

filtered_defense = defense[
    ((defense['team'] == team) | (team == "All")) &
    ((defense['win_loss'] == win_loss) | (win_loss == "All")) &
    ((defense['home_or_away'] == home_or_away) | (home_or_away == "All")) &
    ((defense['year'] == year) | (year == "All"))
]


tab1, tab2 = st.tabs(["Offense", "Defense"])

with tab1:
    st.write(filtered_offense)

with tab2:
    st.write(filtered_defense)
