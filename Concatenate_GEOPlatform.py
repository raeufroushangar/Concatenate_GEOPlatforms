
# Dependencies to import
import os
import pandas as pd

# Concatenate GEO platform files into one main tab delimited text file:
# function inputs:
#-----------------
#1st input: str() -- name of file that will be created
#2nd input: str() -- directory path where GEO platform files are located
#-----------------
def Concatenate_GEOPlatform(file_name, GEOPlatform_files_directory):
    
    # GEO platform files name must have "platform" and same directory
    os.chdir(GEOPlatform_files_directory)
    
    platform_dataframes = []
    # Loop through platform files in directory
    for file in os.listdir():
        if "platform" in file:
            platform_file = pd.read_csv(file, sep="\t") # read file
            platform_dataframes.append(platform_file)   # append file
    
    # Concatenate all dataframes
    result = pd.concat(platform_dataframes)
    # Write data into text file
    result.to_csv(file_name, sep="\t",index=False, encoding='utf-8')


 
Concatenate_GEOPlatform("platform_reference.txt", 
                        'set your directory here where GEO platform files located')