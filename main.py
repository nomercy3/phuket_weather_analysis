from cleaning import prepare_data, make_weather_code_df, calculate_score, grouped_score_by_month, max_score_value_by_month
from analysis import precipitation_score_month, mean_score_month, calc_most_rainy_day
import pandas as pd


data = pd.read_csv('/Users/vasilypopov/developer/jupyter_notebooks/phuket_weather_analysis/Phuket, Weather, Daily 2015-2021.csv')

# Analysis main flow


def main():
    # Clean data
    daily_df = prepare_data(data)

    # Calculate score for each row
    daily_df['Weather Condition Score'] = daily_df.apply(lambda row: calculate_score(daily_df, row, make_weather_code_df(daily_df)), axis=1)

    # Created separate df for aggregated values. It will help us later with the analysis
    aggregated_df = pd.DataFrame(grouped_score_by_month(daily_df))
    aggregated_df.reset_index(inplace=True)
    aggregated_df.rename(columns={'Weather Condition Score': 'Score For Month'}, inplace=True)

    # Created max in month
    aggregated_df['Max In Month'] = max_score_value_by_month(daily_df)['Weather Condition Score']

    precipitation_score_df = precipitation_score_month(aggregated_df)
    precipitation_score_df['Mean Precipitation Score'] = mean_score_month(aggregated_df)['Score For Month']

    # inner join
    analysis_df = pd.merge(
        precipitation_score_df,
        calc_most_rainy_day(daily_df, aggregated_df),
        on=['Date Month']
    )


if __name__ == '__main__':
    main()
