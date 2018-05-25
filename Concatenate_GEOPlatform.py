
# Dependencies
import os
import pandas as pd

# GEO platform files name must have "platform" and same directory
os.chdir('set your directory here where GEO platform files located')

platform_dataframes = []
# Loop through platform files in directory
for file in os.listdir():
    if "platform" in file:
        platform_file = pd.read_csv(file, sep="\t") # read file
        platform_dataframes.append(platform_file)   # append file

# Concatenate all dataframes
result = pd.concat(platform_dataframes)
# Write data into text file
result.to_csv("platform_reference.txt", sep="\t",index=False, encoding='utf-8')

