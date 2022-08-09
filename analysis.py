import pandas as pd


# Calculate most rainy day values and dates for each month
def calc_most_rainy_day(raw_df, grouped_df):
  df: pd.DataFrame = grouped_df.groupby(['Date Month'])['Max In Month'].max().reset_index(name='Most Rainy Day Value')

  dates = list()

  for month, value in zip(
      df['Date Month'].values,
      df['Most Rainy Day Value'].values
  ):
    dates.append(raw_df.loc[
                   (raw_df['Weather Condition Score'] == value) &
                   (raw_df['Date Month'] == month),
                   'Date (String)'
                 ].head(1).item())

  df['Most Rainy Day Date'] = dates

  return df
