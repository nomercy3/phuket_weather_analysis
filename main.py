# Imports
from preparation import prepare_data, make_weather_code_df
from analysis import calc_most_rainy_day
from weather_condition_score import calc_weather_condition_score
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Analysis flow
def main():
    # Cleaning and preparation
    data = pd.read_csv('input/Phuket, Weather, Daily 2015-2021.csv')
    main_df = prepare_data(data)

    # D-7 weather codes dataframe created
    # In order to calculate precipitation, we should assign weight values to the given D-7 codes.
    weather_codes_df = make_weather_code_df()

    # Weather Condition Score
    # Weather Condition Score will be our key metric to define our daily precipitation amount.
    # To calculate it we will define a function, that will sum up values for weather codes in each row.
    main_df['Weather Condition Score'] = main_df.apply(
        lambda row: calc_weather_condition_score(
            main_df,
            row,
            weather_codes_df
        ),
        axis=1
    )

    # Question 1
    # Which month is the best to come to Phuket during the Rain Season (the weather is primarily clear)?
    aggregated_df = pd.DataFrame(
        main_df.groupby(['Date Year', 'Date Month'])['Weather Condition Score'].sum()
    )
    aggregated_df.reset_index(inplace=True)
    aggregated_df.rename(columns={'Weather Condition Score': 'Score For Month'}, inplace=True)
    month_labels = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
    aggregated_df['Date Month Name'] = aggregated_df['Date Month'].apply(lambda row: month_labels[row])
    sns.boxplot(
        x='Date Month Name',
        y='Score For Month',
        data=aggregated_df,
        palette='YlGnBu'
    )
    # Answer:
    # plt.show()
    # It appears July is the best month to come to Phuket during Rain Season.
    # The median value of precipitation amount is the lowest among other months.
    # Also, during regular (sunny) season February is best weather.

    # Question 2
    # Which month has the highest precipitation amount and is therefore not significant to stand by?
    # Based on the previous plot, we could say, that May is the worst month to visit Phuket among all month,
    # because box in the chart is relatively small.

    # Question 3
    # Is rain season worth its name? Is precipitation amount so different?
    # To find an answer I want to calculate mean precipitation score.
    mean_precipitation_df = aggregated_df.groupby([
        'Date Month',
        'Date Month Name'
    ])[
        'Score For Month'
    ].mean().reset_index(name='Mean Precipitation Score')
    sns.lineplot(
        x='Date Month Name',
        y='Mean Precipitation Score',
        data=mean_precipitation_df
    )
    # Answer:
    # plt.show()
    # As we can see, precipitation amount in May is higher by 700% comparing to February.
    # So we could say that yes, the Rain Season worth its name.

    # Question 4
    # What was the rainiest day in the study period?
    # To answer this question first we should calculate Max Precipitation Amount in every month,
    # then find max value among similar months and then retrieve the date for each value.
    aggregated_df['Max In Month'] = main_df.groupby([
        'Date Year',
        'Date Month'
    ])['Weather Condition Score'].max().reset_index()['Weather Condition Score']
    most_rainy_day_df = calc_most_rainy_day(main_df, aggregated_df)
    # Now we can find the maximum value among maximum values and find the rainiest day in study period.
    max_precipitation_date = most_rainy_day_df.loc[
        (most_rainy_day_df['Most Rainy Day Value'] == most_rainy_day_df['Most Rainy Day Value'].max()),
        ['Most Rainy Day Value', 'Most Rainy Day Date']
    ]
    # Answer:
    # print(max_precipitation_date)
    # As we can see, the most rainy day is 10th September 2020 with precipitation amount of 44.


if __name__ == '__main__':
    main()
