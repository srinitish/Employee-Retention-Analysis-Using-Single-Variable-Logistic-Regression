import pandas as pd
import numpy as np
import os

# Change to the correct directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

print(f"Current directory: {os.getcwd()}")
print(f"CSV file exists: {os.path.exists('HR_comma_sep.csv')}")

df = pd.read_csv('HR_comma_sep.csv')
print("\nDataFrame head:")
print(df.head())

print("\nDataFrame info:")
df.info()
