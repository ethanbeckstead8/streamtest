"""
This module scrapes tables from pro-football-reference.com.
"""
import pandas as pd
def get_offensive_game_stats_with_playoffs(base_url, years):
    """Scrapes the offensive tables for the specified years and combines with the playoff tables.
    
    Parameters:
    base_url (str): the url to scrape from.
    years (list of int): list of integers of years where the team played in the playoffs.

    Returns:
    dataframe: The combined offensive data from years the team played in the playoffs.
    """
    all_data = []
    
    for year in years:
        url = base_url.format(year=year)
        tables = pd.read_html(url,  header=[0, 1])
        table_0 = tables[0]
        table_0['Year'] = year
        all_data.append(table_0)
        table_1 = tables[1]
        table_1['Year'] = year
        all_data.append(table_1)
    
    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df


def get_offensive_game_stats_no_playoffs(base_url, years):
    """Scrapes the offensive tables for the specified years.
    
    Parameters:
    base_url (str): the url to scrape from.
    years (list of int): list of integers of years where the team did not play in the playoffs.

    Returns:
    dataframe: The combined offensive data from years the team did not play in the playoffs.
    """
    all_data = []
    
    for year in years:
        url = base_url.format(year=year)
        tables = pd.read_html(url,  header=[0, 1])
        year_data = tables[0]
        year_data['Year'] = year
        all_data.append(year_data)
    
    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df


def get_opp_game_stats_with_playoffs(base_url, years):
    """Scrapes the offensive tables for the specified years of the opponent and combines with the playoff tables.
    
    Parameters:
    base_url (str): the url to scrape from.
    years (list of int): list of integers of years where the team played in the playoffs.

    Returns:
    dataframe: The combined offensive data from years the team played in the playoffs.
    """
    all_data = []
    
    for year in years:
        url = base_url.format(year=year)
        tables = pd.read_html(url,  header=[0, 1])
        table_2 = tables[2]
        table_2['Year'] = year
        all_data.append(table_2)
        table_3 = tables[3]
        table_3['Year'] = year
        all_data.append(table_3)
    
    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df


def get_opp_game_stats_no_playoffs(base_url, years):
    """Scrapes the opponent's offensive tables for the specified years.
    
    Parameters:
    base_url (str): the url to scrape from.
    years (list of int): list of integers of years where the team did not play in the playoffs.

    Returns:
    dataframe: The combined offensive data from years the team did not play in the playoffs.
    """
    all_data = []
    
    for year in years:
        url = base_url.format(year=year)
        tables = pd.read_html(url,  header=[0, 1])
        year_data = tables[1]
        year_data['Year'] = year
        all_data.append(year_data)
    
    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df