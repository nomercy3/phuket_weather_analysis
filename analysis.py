import pandas as pd
from cleaning import preparation


def precipitation_score_month(dataframe: pd.DataFrame):
  return dataframe.groupby(["Date Month"])["Score For Month"].sum().reset_index(name="Precipitation Score")


def mean_score_month(dataframe: pd.DataFrame):
  return dataframe.groupby(["Date Month"])["Score For Month"].mean().reset_index()


def calc_most_rainy_day(dataframe: pd.DataFrame, aggregated: pd.DataFrame):
  max_values: pd.DataFrame = aggregated.groupby(["Date Month"])["Max In Month"].max().reset_index(name="Most Rainy Day (Value)")
  # max_values.rename(columns={"Max In Month": "Most Rainy Day (Value)"}, inplace=True)

  # print(max_values_dates)

  # print(max_values)
