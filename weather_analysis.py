# _*- coding: utf-8 -*-
"""
Created on Tue Apr 12 20:33:16 2022

@author: ENOCH
"""

import pandas as pd
filename = 'Weather_data.csv'
data = pd.read_csv(filename)
#print(data.columns)
unique_wind = data['Wind Speed_km/h'].unique()
print('The Unique wind speed are:',  unique_wind)
clear = data[data['Weather']=='Clear']
print('The number of times when the data is exactly clear is:',
      len(clear))
Exactly_4 = data[data['Wind Speed_km/h']==4]
print('The number of times when the wind speed is exactly 4km/h:',
      len(Exactly_4))
Null_values = data.isnull()
print('total number of null values are:', Null_values.sum())
data.columns = data.columns.str.replace('Weather','Weather_Condition')
data.rename(columns={'Wind Speed_km/h':'Wind_speed'}, inplace=True)
mean_vis = data['Visibility_km'].mean()
print('The mean visibility is:', mean_vis)
std_press = data['Press_kPa'].std()
print('The standard deviation of pressure is:', std_press)
rel_hum = data['Rel Hum_%'].var()
print('The variance of relative humidity is:', rel_hum)
snow_df = data[data['Weather_Condition']=='Snow']
print('\nAll instances where Snow is recorded are below')
print(snow_df)
speed_vis = data.query('Wind_speed > 24 & Visibility_km == 25')
print('\nAll instances where wind speed is above 24 and visibility is 25')
print(speed_vis)
list1 = ['Temp_C', 'Dew Point Temp_C', 'Rel Hum_%',
       'Wind_speed', 'Visibility_km', 'Press_kPa']
group = data.pivot_table(index='Weather_Condition',
                         values=list1,
                         aggfunc='mean')
print('\nThe mean of each column against each weather condition are:')
print(group)
group2 = data.pivot_table(index='Weather_Condition',
                          values=list1,
                          aggfunc=[min, max])
print('\n' + 'The minimum and maximum values for each column'
      + ' against each weather conditions are:')
print(group2)
fog_df = data[data['Weather_Condition']=='Fog']
print('\nAll instances where Fog is recorded are below')
print(fog_df)
inst_2 = data.query('Weather_Condition == "Clear" | Visibility_km > 40')
print('\nWeather is clear, visibility above 40')
print(inst_2)