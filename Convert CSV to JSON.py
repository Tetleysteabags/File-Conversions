# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 13:09:20 2022

@author: Thomas G
"""
import pandas as pd
#Import the CSV file you want to convert
df = pd.read_csv (r'C:\Users\Thoma\Desktop\Coding\YPO Data Connect CSV.csv',encoding="mbcs")
#check the dataset has imported correctly
df.head()
#conver the imported file to JSON and save in the desired location with appropriate name
df.to_json(r'C:\Users\Thoma\Desktop\Coding\Converted YPO Data Connect CSV.json')