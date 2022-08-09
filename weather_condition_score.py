import pandas as pd


# Weather Condition Score calculation
def calc_weather_condition_score(df: pd.DataFrame, row, weather_codes_values_df: pd.DataFrame):
  score = 0

  weather_codes_list = pd.concat([
    df['Weather Code 1 (String)'],
    df['Weather Code 2 (String)'],
    df['Weather Code 3 (String)'],
    df['Weather Code 4 (String)'],
    df['Weather Code 5 (String)'],
    df['Weather Code 6 (String)'],
    df['Weather Code 7 (String)'],
    df['Weather Code 8 (String)'],
    df['Weather Code 9 (String)'],
    df['Weather Code 10 (String)']
  ]).unique().tolist()

  weather_code_columns = [
    'Weather Code 1 (String)',
    'Weather Code 2 (String)',
    'Weather Code 3 (String)',
    'Weather Code 4 (String)',
    'Weather Code 5 (String)',
    'Weather Code 6 (String)',
    'Weather Code 7 (String)',
    'Weather Code 8 (String)',
    'Weather Code 9 (String)',
    'Weather Code 10 (String)'
  ]

  for index, item in enumerate(weather_code_columns):
    if row[item] in weather_codes_list and pd.isna(row[item]) is False:
      score += weather_codes_values_df.loc[
        weather_codes_values_df['Weather Code'] == row[item],
        'Value'
      ].iat[0]
  return score
