import pandas as pd


def prepare_data(data):

    # 1. Columns hided, dataframe selected, duplicates dropped
    df = pd.DataFrame(data, columns=[
        'Date (String)',
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
        'Weather Code 11 (String)',
        'Weather Label 11 (String)',
        'Weather Code 12 (String)',
        'Weather Label 12 (String)'
    ])

    df.drop_duplicates()

    # 2. Null columns dropped
    df.drop(
        columns=[
            'Weather Code 11 (String)',
            'Weather Label 11 (String)',
            'Weather Code 12 (String)',
            'Weather Label 12 (String)'
        ],
        axis=1,
        inplace=True
    )

    # 3. Columns' types checked
    # 'Date (String)' with type string was converted to datetime.2 new columns were created
    # to help us aggregate our data later:
    #     - Date Year
    #     - Date Month
    df['Date (String)'] = pd.to_datetime(df['Date (String)'])
    df['Date Year'] = pd.DatetimeIndex(df['Date (String)']).year
    df['Date Month'] = pd.DatetimeIndex(df['Date (String)']).month

    # 4 Data completeness checked
    # Since we are dealing with time-sensitive data, we should check if the last year contains data for the whole year.
    # 2022 year is not complete, so we should drop it out of our dataframe.
    prepared_df = df[~df['Date Year'].isin([2022])]

    return prepared_df


def make_weather_code_df():

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
        'Value': [
            3, 4, 4, 1, 2, 2, 2, 9, 8, 1, 7,
            5, 1, 2, 6, 4, 5, 4, 3, 3, 3,
            1, 2, 8, 5, 4, 3, 4, 3, 2,
            4, 1, 1, 1, 2, 1, 3, 0, 7, 2, 9,
            2
        ]
    }
    weather_codes_df = pd.DataFrame(weather_codes_values)
    return weather_codes_df
