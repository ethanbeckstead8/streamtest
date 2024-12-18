import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
import plotly.express as px

df = pd.read_csv("nfl_package\datasets\kc_offensive_game_stats_cleaned.csv") 

def make_corr_matrix(df):
    df['win_loss_binary'] = [1 if x == 'W' else 0 for x in df['win_loss']]
    columns_to_drop = ['week', 'day', 'date', 'win_loss', 'OT', 'opp', 'year', 'home_or_away']
    df_temp = df.drop(columns=columns_to_drop, axis=1)
    corr_matrix = df_temp.corr()
    return corr_matrix


def win_correlations(corr_matrix):
    mat = corr_matrix['win_loss_binary'].sort_values(ascending=False)
    print("Correlation with Win/Loss (top 5):")
    print(mat[1:6])
    wins_descriptive_stats = df[mat[1:6].index].describe()
    print("\nDescriptive Statistics for Top 5 Variables correlated with wins:")
    print(wins_descriptive_stats)
    return mat



def score_correlations(corr_matrix):
    mat = corr_matrix['pts_scored'].sort_values(ascending=False)
    print("Correlation with Points Scored (top 5):")
    print(mat[1:6])
    points_descriptive_stats = df[mat[1:6].index].describe()
    print("\nDescriptive Statistics for Top 5 Variables correlated with points scored:")
    print(points_descriptive_stats)
    return mat


kc_mat = make_corr_matrix(df)
win_correlations(kc_mat)
score_correlations(kc_mat)


def generate_top5_plots(df, win_correlations):
    top_5_vars = win_correlations[1:6].index
    grouped_stats = df.groupby('win_loss_binary')[top_5_vars].describe()
    plots = []
    for var in top_5_vars:
        fig, ax = plt.subplots()
        sns.boxplot(x='win_loss_binary', y=var, data=df, ax=ax)
        ax.set_title(f"{var} by Win/Loss")
        ax.set_xlabel("Game Result")
        ax.set_ylabel(f"{var}")
        plots.append(fig)
    
    return grouped_stats, plots


#plt.figure(figsize=(25, 20))
#sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
#plt.title('Correlation Matrix Heatmap')
#plt.show()

import matplotlib.pyplot as plt
import numpy as np


# Boxplot
def top_boxplot(df):
    win_data = df[df['win_loss_binary'] == 1]['off_top']
    loss_data = df[df['win_loss_binary'] == 0]['off_top']
    data = [win_data, loss_data]
    
    fig = plt.figure(figsize =(10, 7))
    ax = fig.add_axes([0, 0, 1, 1])
    
    bp = ax.boxplot(data, patch_artist=True, labels=['Wins', 'Losses'])
    ax.set_title('Boxplot of Time of Possession for Wins and Losses')
    ax.set_ylabel('Time of Possession')
    ax.set_xlabel('Game Result')

    colors = ['blue', 'red']
    for box, color in zip(bp['boxes'], colors):
        box.set(facecolor=color, alpha=0.5) 

    positions = [1, 2]
    for pos, dataset, color in zip(positions, data, colors):
        jittered_x = np.random.normal(pos, 0.025, size=len(dataset))
        ax.scatter(jittered_x, dataset, alpha=0.6, color=color)

    plt.show()

top_boxplot(df)