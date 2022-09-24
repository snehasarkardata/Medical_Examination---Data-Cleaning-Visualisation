# Medical_Examination---Data-Cleaning-Visualisation
medical_examination data set contains 70000 rows, 13 attributes where the columns are named as 	id,	age,	sex,	height,	weight,	ap_hi,	ap_lo,	cholesterol,	gluc,	smoke,	alco,	active,	cardio.

Library used:
1) numpy as np
2) seaborn as sns
3) pandas as pd
4) matplotlib.pyplot as plt

Purpose:
Use the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

Steps:
1) Add an overweight column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
   Normalize the data by making 0 always good and 1 always bad. 
2) If the value of cholesterol or gluc is 1, make the value 0. If the value is more than 1, make the value 1.
3) Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's catplot().
4)  The dataset should be split by 'Cardio' so there is one chart for each cardio value. 
5)  Clean the data. Filter out the following patient segments that represent incorrect data:
diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
- height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
- height is more than the 97.5th percentile
- weight is less than the 2.5th percentile
- weight is more than the 97.5th percentile
6) Create a correlation matrix using the dataset. Plot the correlation matrix using seaborn's heatmap().
