import pandas as pd
from lists import *

'''
1. Columns Hided:
- Call Sign
- Time Zone (ID)
- Temperature Sampled Low (°C)
- Temperature Sampled High (°C)
- Dew Point Sampled Low (°C)
- Dew Point Sampled High (°C) 
- Wind Speed Min (kph)
- Wind Speed Max (kph)
- Gust Speed Max (kph)
- Visibility Min (km)
- Visibility Max (km)
- Precipitation (mm)
- Snow Depth Max (mm)
- Pressure Altimeter Min (mbar)
- Pressure Altimeter Max (mbar)
- Min Cloud Layer Code (String)
- Min Cloud Layer Label (String)
- Max Cloud Layer Code (String)
- Max Cloud Layer Label (String)
'''

'''
2. Duplicates dropped
'''

'''
3. Convert Date (String) to datetime, create year and month columns for further calculations, drop 2022
'''

'''
4. Count reports to make sure it is equal to the number of days in months. 
'''


def prepare_data(data):

    # 1. Columns hided, dataframe selected
    df = pd.DataFrame(data, columns=[
        'Date (String)',
        'Wind Direction Dominant (degrees)',
        'Weather Code 1 (String)',
        'Weather Label 1 (String)',
        'Weather Code 2 (String)',
        'Weather Label 2 (String)',
        'Weather Code 3 (String)',
        'Weather Label 3 (String)',
        'Weather Code 4 (String)',
        'Weather Label 4 (String)',
        'Weather Code 5 (String)',
        'Weather Label 5 (String)',
        'Weather Code 6 (String)',
        'Weather Label 6 (String)',
        'Weather Code 7 (String)',
        'Weather Label 7 (String)',
        'Weather Code 8 (String)',
        'Weather Label 8 (String)',
        'Weather Code 9 (String)',
        'Weather Label 9 (String)',
        'Weather Code 10 (String)',
        'Weather Label 10 (String)',
        'Weather Condition Score'
    ])

    # 2 Duplicates dropped
    df.drop_duplicates()

    # 3. Converting variables
    df['Date (String)'] = pd.to_datetime(df['Date (String)'])
    df['Date Year'] = pd.DatetimeIndex(df['Date (String)']).year
    df['Date Month'] = pd.DatetimeIndex(df['Date (String)']).month
    prepared_df = df[~df['Date Year'].isin([2022])]

    # 4. Check for records in months
    group_by_month_and_year = df.groupby(['Date Year', 'Date Month'])['Date (String)'].count()

    return prepared_df


def make_weather_code_df(dataframe):

    weather_codes_values = {
        'Weather Code': [
            '-RA', 'TS', 'RA', 'BR', 'RERA', 'HZ', 'RETS', '+TSRA', 'TSRA', 'VCSH', '-TSRA',
            '+RA', 'VCTS', 'RETSRA', '+SHRA', 'IWC17', 'IWC65', 'IWC21', 'IWC60', '-TS', '-DZ',
            'IWC13', 'MIFG', 'IWC95', 'SHRA', 'IWC63', 'IWC61', 'DZ', 'IWC51', 'RESHRA',
            '-SHRA', 'IWC10', '-BR', 'BCFG', 'FG', 'IWC16', 'FU', 'RE', 'PO', 'REDZ', 'FC',
            'REFC'
        ],
        'Weather Label': [
            'light rain', 'thunderstorm', 'rain', 'mist', 'recent rain', 'haze', 'recent thunderstorm',
            'thunderstorm with heavy rain', 'thunderstorm with rain', 'showers in the vicinity',
            'thunderstorm with light rain', 'heavy rain', 'thunderstorm in the vicinity',
            'recent thunderstorm with rain', 'showers of heavy rain', 'thunderstorm', 'heavy rain',
            'rain', 'light intermittent rain', 'mild thunderstorm', 'light drizzle',
            'thunderstorm in the vicinity', 'shallow fog', 'thunderstorm with rain', 'showers of rain',
            'rain', 'light rain', 'drizzle', 'light drizzle', 'recent showers of rain', 'showers of light rain',
            'mist', 'light mist', 'patches of fog', 'fog', 'precipitation in the vicinity', 'smoke',
            'recent unknown weather', 'well-developed dust/sand whirls', 'recent drizzle', 'funnel cloud',
            'recent funnel cloud'
        ],
        'Scores': [
            3, 4, 4, 1, 2, 2, 2, 9, 8, 1, 7,
            5, 1, 2, 6, 4, 5, 4, 3, 3, 3,
            1, 2, 8, 5, 4, 3, 4, 3, 2,
            4, 1, 1, 1, 2, 1, 3, 0, 7, 2, 9,
            2
        ]
    }
    weather_codes_scores_df = pd.DataFrame(weather_codes_values)
    return weather_codes_scores_df



def calculate_score(dataframe: pd.DataFrame, row, values_to_match: pd.DataFrame):
    score = 0

    weather_codes_list = pd.concat([
        dataframe['Weather Code 1 (String)'],
        dataframe['Weather Code 2 (String)'],
        dataframe['Weather Code 3 (String)'],
        dataframe['Weather Code 4 (String)'],
        dataframe['Weather Code 5 (String)'],
        dataframe['Weather Code 6 (String)'],
        dataframe['Weather Code 7 (String)'],
        dataframe['Weather Code 8 (String)'],
        dataframe['Weather Code 9 (String)'],
        dataframe['Weather Code 10 (String)']
    ]).unique().tolist()

    for index, item in enumerate(weather_code_columns):
        if row[item] in weather_codes_list and pd.isna(row[item]) is False:
            score += values_to_match.loc[values_to_match['Weather Code'] == row[item], 'Scores'].iat[0]
    return score


'''
Scores were aggregated by each month and year — this gives us the summary of all scores by month
'''


def grouped_score_by_month(dataframe: pd.DataFrame):
    return dataframe.groupby(['Date Year', 'Date Month'])['Weather Condition Score'].sum()


def max_score_value_by_month(dataframe: pd.DataFrame):
    return dataframe.groupby(['Date Year', 'Date Month'])['Weather Condition Score'].max().reset_index()
