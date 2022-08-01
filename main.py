from cleaning import preparation, make_weather_code_table, calculate_score, grouped_score_by_month, max_score_value_by_month
from analysis import precipitation_score_month, mean_score_month, calc_most_rainy_day
import pandas as pd


data = pd.read_csv('/Users/vasilypopov/developer/jupyter_notebooks/phuket_weather_analysis/Phuket, Weather, Daily 2015-2021.csv')


def main():
    # Clean data
    daily_df = preparation(data)

    # Calculate score for each row
    daily_df["Weather Condition Score"] = daily_df.apply(lambda row: calculate_score(daily_df, row, make_weather_code_table(daily_df)), axis=1)

    # Created separate df for aggregated values. Helping us later with analysis
    aggregated_df = pd.DataFrame(grouped_score_by_month(daily_df))
    aggregated_df.reset_index(inplace=True)
    aggregated_df.rename(columns={"Weather Condition Score": "Score For Month"}, inplace=True)

    # Created max in month
    aggregated_df["Max In Month"] = max_score_value_by_month(daily_df)["Weather Condition Score"]

    analysis_df = precipitation_score_month(aggregated_df)
    analysis_df["Mean Precipitation Score"] = mean_score_month(aggregated_df)["Score For Month"]
    print(aggregated_df)
    print(analysis_df)
    calc_most_rainy_day(daily_df, aggregated_df)


if __name__ == '__main__':
    main()
