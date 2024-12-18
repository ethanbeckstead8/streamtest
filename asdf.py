import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


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

year_range = st.sidebar.slider(
    "Year Range",
    min_value=int(offense['year'].min()),
    max_value=int(offense['year'].max()),
    value=(int(offense['year'].min()), int(offense['year'].max())),
)


filtered_offense = offense[
    ((offense['team'] == team) | (team == "All")) &
    ((offense['win_loss'] == win_loss) | (win_loss == "All")) &
    ((offense['home_or_away'] == home_or_away) | (home_or_away == "All")) &
    (offense['year'].between(year_range[0], year_range[1]))
]

filtered_defense = defense[
    ((defense['team'] == team) | (team == "All")) &
    ((defense['win_loss'] == win_loss) | (win_loss == "All")) &
    ((defense['home_or_away'] == home_or_away) | (home_or_away == "All")) &
    (defense['year'].between(year_range[0], year_range[1]))
]


ot_games = filtered_offense[filtered_offense['OT'] == 'OT']
ot_percentage = (len(ot_games) / len(filtered_offense)) * 100
avg_punts = filtered_offense['times_punted'].mean()
avg_rush_tds = filtered_offense['rushing_tds'].mean()
avg_pass_tds = filtered_offense['passing_tds'].mean()
avg_fgm = filtered_offense['fgm'].mean()
fg_percentage = (filtered_offense['fgm'].sum() / filtered_offense['fga'].sum()) * 100 if filtered_offense['fga'].sum() != 0 else 0
third_down_pct = (filtered_offense['3dconv'].sum() / filtered_offense['3dattempt'].sum()) * 100 if filtered_offense['3dattempt'].sum() != 0 else 0
fourth_down_pct = (filtered_offense['4dconv'].sum() / filtered_offense['4datt'].sum()) * 100 if filtered_offense['4datt'].sum() != 0 else 0
points_for = filtered_offense['pts_scored'].sum()
points_against = filtered_offense['pts_allowed'].sum()
passer_rating = filtered_offense['passer_rating'].mean()
ry_a = filtered_offense['rushing_yds/attempt'].mean()
py_a = filtered_offense['yds/pass_attempt'].mean()


st.subheader("Filtered Statistics")
st.write(f"Overtime Percentage: {ot_percentage:.2f}%")
st.write(f"Average Punts: {avg_punts:.2f}")
st.write(f"Average Rush TDs: {avg_rush_tds:.2f}")
st.write(f"Average Pass TDs: {avg_pass_tds:.2f}")
st.write(f"Average FGM: {avg_fgm:.2f}")
st.write(f"Field Goal Percentage: {fg_percentage:.2f}%")
st.write(f"3rd Down Completion Percentage: {third_down_pct:.2f}%")
st.write(f"4th Down Completion Percentage: {fourth_down_pct:.2f}%")
st.write(f"Points For: {points_for}")
st.write(f"Points Against: {points_against}")
st.write(f"Passer Rating: {passer_rating:.2f}")
st.write(f"Rushing Yards per Attempt: {ry_a:.2f}")
st.write(f"Passing Yards per Attempt: {py_a:.2f}")
tab1, tab2 = st.tabs(["Offense", "Defense"])



with tab1:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(filtered_offense['passing_yds'], filtered_offense['rushing_yds_gained'], color='darkblue', alpha=0.75)
    ax.set_title("Passing Yards vs Rushing Yards Gained (Offense)")
    ax.set_xlabel("Passing Yards")
    ax.set_ylabel("Rushing Yards Gained")
    st.pyplot(fig)
    st.write(filtered_offense)

with tab2:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(filtered_defense['passing_yds'], filtered_defense['rushing_yds_gained'], color='hotpink', alpha=0.75)
    ax.set_title("Passing Yards vs Rushing Yards Gained (Defense)")
    ax.set_xlabel("Passing Yards")
    ax.set_ylabel("Rushing Yards Gained")
    st.pyplot(fig)
    st.write(filtered_defense)
