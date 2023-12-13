# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 20:49:43 2023

@author: fahme
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#link https://data.worldbank.org/indicator/AG.PRD.CROP.XD?view=chart

file = pd.read_csv("data.csv")
print("Data before cleaning")
print(file.head())


def filename(file1):
    '''
    Function to load a World Bank dataset, clean it and transform it into two
    dataframes:
    1. Original dataframe.
    2. Transposed dataframe.

    Args:
    file1: The file path to the Excel file that we have to work.

    Returns:
    tuple: A tuple containing the two pandas dataframes.
    
    '''
    filter_data= file1[["Country Name", "1965", "1970", "1975", "1980", "1985", 
                       "1990", "1995", "2000", "2005", "2010", "2015", "2020"]]
    filter_data.dropna(inplace=True)
    data_O= filter_data
    data_T= filter_data.transpose()
    return data_O, data_T


def stats(file1):
    '''
    Function to do basic statistics analysis by describe method and print it
    
    Args:
    file1: Any clean dataframe which we want statistics 

    '''
    stats_analysis = file1.describe()
    print("Statistics Summary:")
    print(data_O.describe())
    return



# Printing few rows of 2 datas
data_O, data_T= filename(file)
print("\t \t \t AFTER CLEAN")
print("Original Data:")
print(data_O.head())
print()
print("Transposed Data:")
print(data_T.head())
print()

# Printing basic statistics
stats(data_O)


    

#Europe: Sweden, Switzerland, Germany, France, Spain, Portugal
#Asia: Afghanistan, Japan, India, Pakistan, Kuwait, Iraq
#South America: Brazil, Colombia, Paraguay, Uruguay, Mexico, Venezuela
#Africa: Angola, Algeria, Egypt, Ghana, Kenya, Libya, Somalia, Zimbabwe


Europe= data_O.loc[data_O["Country Name"].isin(['Sweden', 'Switzerland', 
                                                    'Spain','France', 
                                                    'Portugal'])]
Europe_T = Europe.set_index('Country Name').T
#print(Europe_T)

Asia= data_O.loc[data_O["Country Name"].isin(['Japan', 'India', 
                                                  'Pakistan', 'Kuwait', 
                                                  'Iraq'])]
Asia_T = Asia.set_index('Country Name').T
#print(Asia_T)

S_America= data_O.loc[data_O["Country Name"].isin(['Venezuela', 'Paraguay', 
                                                    'Colombia', 'Uruguay', 
                                                    'Brazil'])]
S_America_T = S_America.set_index('Country Name').T
#print(S_America_T)

Africa= data_O.loc[data_O["Country Name"].isin(['Angola', 'Ghana', 'Kenya',
                                                    'Somalia', 'Zimbabwe'])]
Africa_T = Africa.set_index('Country Name').T
#print(Africa)

# Correlation
print()
print("Correlation of European countries:")
print(Europe_T.corr())
print()
print("Correlation of African countries:")
print(Africa_T.corr())
print()



# #Bar chart
Asia_bar = Asia[["Country Name", "1985", "1990", "1995", "2000", "2005", 
                 "2010", "2015", "2020"]]
plt.figure()
Asia_bar.plot(x= "Country Name", kind='bar', figsize=(12,8))
plt.title("Crop Production in Asian countries(1985-2020)", fontweight="bold")
plt.xlabel("Countries", fontweight="bold")
plt.ylabel("Production amount in millions ($)", fontweight="bold")
plt.xticks(rotation=0)
i = np.arange(20, 161, 20)
plt.yticks(i)
plt.legend(loc='upper right', ncol=4)
plt.show()


Europe_bar = Europe[["Country Name", "1985", "1990", "1995", "2000", "2005", 
                 "2010", "2015", "2020"]]
plt.figure()
Europe_bar.plot(x= "Country Name", kind='bar', figsize=(12,8))
plt.title("Crop Production in European countries(1985-2020)", 
          fontweight="bold")
plt.xlabel("Countries", fontweight="bold")
plt.ylabel("Production amount in millions ($)", fontweight="bold")
plt.xticks(rotation=0)
i = np.arange(20, 161, 20)
plt.yticks(i)
plt.legend(loc='upper right', ncol=4)
plt.show()



# Line plot

plt.figure()
Africa_T.plot(kind='line', figsize=(11,7))
plt.title("Crop Production in Afrian Countries", fontweight="bold")
plt.xlabel("Years", fontweight="bold")
plt.ylabel("Production amount in millions ($)", fontweight="bold")
plt.legend(loc='upper left', ncol=5)
i = np.arange(20, 160, 20)
plt.yticks(i)
plt.margins(x=0)
plt.show()

plt.figure()
S_America_T.plot(kind='line', figsize=(11,7))
plt.title("Crop Production in South American countries", fontweight="bold")
plt.xlabel("Years", fontweight="bold")
plt.ylabel("Production amount in millions ($)", fontweight="bold")
plt.legend(loc='upper left', ncol=5)
i = np.arange(20, 160, 20)
plt.yticks(i)
plt.margins(x=0)
plt.show()



# heatmap

plt.figure(figsize=(10,6))
#sns.heatmap(Europe_T)
sns.heatmap(Asia_T.corr(), cmap="YlGnBu", annot=True)
plt.title("Heatmap of Asian countries", fontweight="bold")
plt.show()

plt.figure(figsize=(10,6))
sns.heatmap(S_America_T.corr(), cmap="YlGnBu", annot=True)
plt.title("Heatmap of South American countries", fontweight="bold")
plt.show()



