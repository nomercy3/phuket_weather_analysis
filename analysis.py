import pandas as pd


def precipitation_score_month(dataframe: pd.DataFrame):
  return dataframe.groupby(['Date Month'])['Score For Month'].sum().reset_index(name='Precipitation Score')


def mean_score_month(dataframe: pd.DataFrame):
  return dataframe.groupby(['Date Month'])['Score For Month'].mean().reset_index()


def calc_most_rainy_day(dataframe: pd.DataFrame, aggregated: pd.DataFrame):
  max_values_df: pd.DataFrame = aggregated.groupby(['Date Month'])['Max In Month'].max().reset_index(name='Most Rainy Day (Value)')

  dates = list()
  for month, value in zip(
      max_values_df['Date Month'].values,
      max_values_df['Most Rainy Day (Value)'].values
  ):

    dates.append(dataframe.loc[
      (dataframe['Weather Condition Score'] == value) &
      (dataframe['Date Month'] == month),
      'Date (String)'
    ].head(1).item())

  max_values_df['Most Rainy Day (Date)'] = dates

  return max_values_df
