# Phuket Precipitation Analysis

## Intro

 1. Sunny Season, during which all of the regular tourists come.
 2. Rain Season — the weather is unpredictable and can ruin your trip. The waves are generally high, and it's not allowed to swim in the sea.

I started this project because my family is coming to Phuket to visit me during the rainy season. I was pretty concerned about the precipitation amount these days because they wanted to have fun on the beach too. However, in general, "Rain Season" is from May till the end of October; my family's trip dates are from 07.07 till 22.07. Further, I will be more focused on these dates (i.g. month — July) from a historical perspective.


## Questions to be answered

 1. Which month is the best to come to Phuket during the Rain Season (the weather is primarily clear)?
 2. Which month has the highest precipitation amount and is therefore not significant to stand by?
 3. Is rain season worth its name? Is precipitation amount so different?
 4. What was the rainiest day in the Rain Season?


## Disclaimer

In this case study, I will use the Code Table D-7: Aerodrome present or forecast weather because the dataset source — Phuket International Airport (many thanks for their work), and use D-7 Codes. You can read more about these weather codes and their use-cases; the link is above.
However, Code Table D-7 is rich in codes, there are no weights to these codes, so I assigned weight values to each code by myself, based on open sources and precipitation amount info.

## Dataset

As mentioned above, the dataset is from Phuket International Airport, which reports on the weather daily and is the only open (paid) source of weather conditions on the island. I bought this dataset from Weather Spark. The study period covers 2015-2021 years. I could've taken a much broader period, but climate change will affect the study outcome.
There is a lot of info in this dataset, but we will use mostly 12 columns of Weather codes (and labels). Each column represents 2 hours of weather condition observation.

## Process
Process flow described in the main.py. Have a look!
