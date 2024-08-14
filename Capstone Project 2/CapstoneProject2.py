'''
Start doing this project on 13 July 2024
finish this project on 24 July 2024

The code was done in Google Colab

Youth Unemplolability:
1)Age
2)State
3)Gender
4)Education Attainment
'''


'''
Data Collection
byYouthAge.csv: Youth unemployment from

byYouthAge.csv = age 15 to 24 years old.
byEduAttainment.csv: Unemployment data by educational attainment.
byGender.csv: Unemployment data by gender.
byStates.csv: Unemployment data by states.
'''

# To import file from google drive
#import os
from google.colab import drive

# Mount Google Drive
#drive.mount('/content/drive', force_remount=True)

# Create a folder in the root directory
#!mkdir -p "/content/drive/MyDrive/usedforeal"

# data cleaning
# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from google.colab import files


# by age
# Read Dataset
print('-' * 90)
print('Read Dataset')
print('-' * 90)
#byYouthAge = pd.read_csv('/content/drive/MyDrive/usedforeal/byYouthAge.csv')  # to mount from drive
byYouthAge = pd.read_csv('byYouthAge.csv')  # for when uploading file
print(byYouthAge)

# drop unnecessary column
print('-' * 90)
print("After drop multiple unnecessary columns")
print('-' * 90)
#byYouthAge.drop(columns=['Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5'], inplace=True)
print(byYouthAge)

# check null
print('-' * 90)
print("check null values")
print('-' * 90)
print(byYouthAge.isnull().sum())

# to check duplicate
print('-' * 90)
print("check duplicate values")
print('-' * 90)
byYouthAge.duplicated().sum()

# to check datatype
print('-' * 90)
print("check datatype")
print('-' * 90)
byYouthAge.dtypes


# to sort Year
print('-' * 90)
print("sort Year")
print('-' * 90)
byYouthAge['Year'] = pd.to_numeric(byYouthAge['Year'], errors='coerce')
filt_byYouthAge = byYouthAge[(byYouthAge['Year'] >= 2001) & (byYouthAge['Year'] <= 2020)]
byYouthAge = filt_byYouthAge
byYouthAge.sort_values(by='Year', inplace=True, ascending=False)
print(byYouthAge.head(6))

# to reset index
print('-' * 90)
print("to reset index")
print('-' * 90)
byYouthAge.reset_index(drop=True, inplace=True)
print(byYouthAge.head(7))

# to rename column
print('-' * 90)
print("to rename column")
print('-' * 90)
byYouthAge.columns=['Gender', 'Year', 'Youth Unemployment']
print(byYouthAge.head(6))


# by education attainment
# Read Dataset
print('-' * 90)
print('Read Dataset')
print('-' * 90)
#byEduAtt = pd.read_csv('/content/drive/MyDrive/usedforeal/byEduAttainment.csv') # to mount from drive
byEduAtt = pd.read_csv('byEduAttainment.csv') # for when uploading file
print(byEduAtt)

# check null
print('-' * 90)
print("check null values")
print('-' * 90)
print(byEduAtt.isnull().sum())

# to check duplicate
print('-' * 90)
print("check duplicate values")
print('-' * 90)
byEduAtt.duplicated().sum()

# to check datatype
print('-' * 90)
print("check datatype")
print('-' * 90)
byEduAtt.dtypes

# to sort Year
print('-' * 90)
print("sort Year")
print('-' * 90)
byEduAtt['Year'] = pd.to_numeric(byEduAtt['Year'], errors='coerce')
filt_byEduAtt = byEduAtt[(byEduAtt['Year'] >= 2001) & (byEduAtt['Year'] <= 2020)]
byEduAtt = filt_byEduAtt
print(byEduAtt.head(6))

# to reset index
print('-' * 90)
print("to reset index")
print('-' * 90)
byEduAtt.reset_index(drop=True, inplace=True)
print(byEduAtt.head(7))

# to rename column
print('-' * 90)
print("to rename column")
print('-' * 90)
byEduAtt.columns=['Year', 'Gender', 'Educational Attainment', 'Percentage']
print(byEduAtt.head(6))

#by gender
# Read Dataset
print('-' * 90)
print('Read Dataset')
print('-' * 90)
#byGender = pd.read_csv('/content/drive/MyDrive/usedforeal/byGender.csv')  # to mount from drive
byGender = pd.read_csv('byGender.csv')  # for when uploading file
print(byGender.head(6))

# check null
print('-' * 90)
print("check null values")
print('-' * 90)
print(byGender.isnull().sum())

# to check duplicate
print('-' * 90)
print("check duplicate values")
print('-' * 90)
byGender.duplicated().sum()

# to check datatype
print('-' * 90)
print("check datatype")
print('-' * 90)
byGender.dtypes


# to sort Year
print('-' * 90)
print("sort Year")
print('-' * 90)
byGender['Year'] = pd.to_numeric(byGender['Year'], errors='coerce')
filt_byGender = byGender[(byEduAtt['Year'] >= 2001) & (byGender['Year'] <= 2020)]
byGender = filt_byGender
print(byGender.head(6))

# to reset index
print('-' * 90)
print("to reset index")
print('-' * 90)
byGender.reset_index(drop=True, inplace=True)
print(byGender.head(7))

# to rename column
print('-' * 90)
print("to rename column")
print('-' * 90)
byGender.columns=['Year', 'Gender', 'Number of Person in Thousand', 'Percentage']
print(byGender.head(6))


# by state
## Read Dataset
print('-' * 90)
print('Read Dataset')
print('-' * 90)
#byStates = pd.read_csv('/content/drive/MyDrive/usedforeal/byStates.csv')  # to mount from drive
byStates = pd.read_csv('byStates.csv')  # for when uploading file
print(byStates)

# check null
print('-' * 90)
print("check null values")
print('-' * 90)
print(byStates.isnull().sum())

# to check duplicate
print('-' * 90)
print("check duplicate values")
print('-' * 90)
byStates.duplicated().sum()

# to check datatype
print('-' * 90)
print("check datatype")
print('-' * 90)
byStates.dtypes


# Data analysis 
# Descriptive Statistics
# describe by Age
print('-' * 90)
print("describe by Age")
print('-' * 90)
pd.set_option('display.float_format',lambda x: '%.2f' % x )
print(byYouthAge['Youth Unemployment'].describe())

# describe by EduAtt
print('-' * 90)
print("describe by EduAtt")
print('-' * 90)
pd.set_option('display.float_format',lambda x: '%.2f' % x )
print(byEduAtt['Percentage'].describe())

# describe by Gender
print('-' * 90)
print("describe by Gender")
print('-' * 90)
pd.set_option('display.float_format',lambda x: '%.2f' % x )
print(byGender[['Number of Person in Thousand', 'Percentage']].describe())

# describe by States
print('-' * 90)
print("describe by States")
print('-' * 90)
pd.set_option('display.float_format',lambda x: '%.2f' % x )
print(byStates['Unemployed Person in Thousand'].describe())


# Trend Analysis
# Overall Trend of Youth Unemployment Over Time
sns.set(style="dark")

plt.figure(figsize=(12, 7))
for gender in byYouthAge['Gender'].unique():
    gender_data = byYouthAge[byYouthAge['Gender'] == gender]
    sns.lineplot(data=gender_data, x=gender_data['Year'].astype(int), y='Youth Unemployment', marker='o', label=gender)

plt.title('Youth Unemployment Rate by Gender (2001-2020)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Youth Unemployment Rate (%)', fontsize=14)
plt.legend(title='Gender', fontsize=12)
plt.grid(True)
plt.xticks(range(min(byYouthAge['Year']), max(byYouthAge['Year'])+1))  # Set integer ticks on x-axis
plt.show()


# Assuming 'Year' column is already numeric (int or float)

# Set Seaborn style
sns.set(style="dark")

# Create figure and axes
plt.figure(figsize=(12, 7))

# Iterate over unique educational attainment levels
for edu_attainment in byEduAtt['Educational Attainment'].unique():
    # Filter data for the current educational attainment level
    edu_data = byEduAtt[byEduAtt['Educational Attainment'] == edu_attainment]
    # Plot line for the current educational attainment level
    sns.lineplot(data=edu_data, x='Year', y='Percentage',marker='o', label=edu_attainment, ci=None, linestyle=None)

# Set plot title and labels
plt.title('Youth Unemployment Rate by Educational Attainment (2001-2020)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Unemployment Rate (%)', fontsize=14)

# Adjust legend and grid
plt.legend(title='Educational Attainment', fontsize=12)
plt.grid(True)
plt.xticks(range(min(byEduAtt['Year']), max(byEduAtt['Year'])+1))  # Set integer ticks on x-axis
plt.show()

# Show the plot
plt.tight_layout()  # Ensures all elements fit within the figure area
plt.show()


# Visualize unemployment trends over time
plt.figure(figsize=(15, 6))

# Aggregating unemployment data by year
unemployment_trends = byStates.groupby('Year')['Unemployed Person in Thousand'].sum()

# Plotting the trend
plt.plot(unemployment_trends.index, unemployment_trends.values, marker='o', linestyle='-')
plt.title('Total Unemployment Trends Over Time (2001-2020)')
plt.xlabel('Year')
plt.ylabel('Unemployed Persons (in Thousands)')
plt.grid(True)
plt.xticks(range(min(byStates['Year']), max(byStates['Year'])+1))
plt.show()


# comparative analysis
# Load the data again
#byStates = pd.read_csv('/content/drive/MyDrive/usedforeal/byStates.csv')  # to mount from drive
byStates = pd.read_csv('byStates.csv')  # for when uploading file

# Calculate the average unemployment rate for each state
state_unemployment_avg = byStates.groupby('States')['Unemployed Person in Thousand'].mean().sort_values()

# Plotting the average unemployment rate by state
fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.barh(state_unemployment_avg.index, state_unemployment_avg.values, color='skyblue')

# Adding the unemployment values on the bars
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.5, bar.get_y() + bar.get_height()/2, round(width, 2), ha='center', va='center')

ax.set_xlabel('Average Unemployed Persons (in Thousands)')
ax.set_title('Average Unemployment Rate by State')
plt.show()


# Verify the column names in the dataset
latest_byStates = byStates.columns=['Year', 'States', 'Unemployed Person in Thousand']

# Identify the most recent year in the dataset
most_recent_year = byStates['Year'].max()

# Filter the data for the most recent year
most_recent_data = byStates[byStates['Year'] == most_recent_year]

# Create a bar chart to compare unemployment rates across states
plt.figure(figsize=(14, 8))
sns.barplot(data=most_recent_data, x='States', y='Unemployed Person in Thousand', palette='viridis')
plt.title(f'Youth Unemployment Rates by State in {most_recent_year}', fontsize=16)
plt.xlabel('States', fontsize=14)
plt.ylabel('Unemployed Person in Thousand', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.grid(True)
plt.show()


# Assuming you have already identified the most recent year correctly
latest_year = byEduAtt['Year'].max()

# Filter the data for the most recent year
latest_byEduAtt = byEduAtt[byEduAtt['Year'] == latest_year]

# Create a bar chart to compare unemployment rates across educational attainment levels
plt.figure(figsize=(14, 8))
sns.barplot(data=latest_byEduAtt, x='Educational Attainment', y='Percentage', ci=None, palette='viridis')
plt.title(f'Youth Unemployment Rates by Educational Attainment in {latest_year}', fontsize=16)  # Adjusted title string
plt.xlabel('Educational Attainment', fontsize=14)
plt.ylabel('Unemployment Rate (%)', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.grid(True)
plt.tight_layout()  # Ensures all elements fit within the figure area
plt.show()


# byEduAtt = pd.read_csv('/content/drive/MyDrive/usedforeal/byEduAttainment.csv') # to mount from drive
# byEduAtt = pd.read_csv('byEduAttainment.csv') # for when uploading file
# print(byEduAtt.head())

# Filter the latest year data
latest_year = byEduAtt['Year'].max()
latest_year_data = byEduAtt[byEduAtt['Year'] == latest_year]

# Print the column names to verify
print(latest_year_data.columns)

# Pivot the data for easier plotting, adjust column name if necessary
pivot_data = latest_year_data.pivot(index='Educational Attainment', columns='Gender', values='Percentage') # Verify 'Educational Attainment' is the correct column name

# Plot the bar chart for educational attainment by gender
plt.figure(figsize=(10, 6))
pivot_data.plot(kind='bar')
plt.title(f'Educational Attainment by Gender in {latest_year}')
plt.xlabel('Educational Attainment')
plt.ylabel('Percentage')
plt.xticks(rotation=45)
plt.legend(title='Gender')
plt.tight_layout()
plt.show()


# Correlation Analysis
#Correlation Between Educational Attainment Levels And Youth Unemployment
# Ensure Year column is of integer type
byEduAtt['Year'] = byEduAtt['Year'].astype(int)
byYouthAge['Year'] = byYouthAge['Year'].astype(int)

# Summarize educational attainment by specific levels
edu_attainment_levels = byEduAtt.pivot_table(index=['Year', 'Gender'], columns='Educational Attainment', values='Percentage', aggfunc='mean').reset_index()

# Merge datasets by Year and Sex
merged_df = pd.merge(edu_attainment_levels, byYouthAge, on=['Year', 'Gender'])
numeric_cols = merged_df.select_dtypes(include=['float64', 'int64']).columns
# Calculate correlation matrix
correlation_matrix = merged_df[numeric_cols].corr()

# Visualization: Correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Between Educational Attainment Levels and Youth Unemployment')


# Ensure Year column is of integer type
byEduAtt['Year'] = byEduAtt['Year'].astype(int)
byYouthAge['Year'] = byYouthAge['Year'].astype(int)

# Summarize educational attainment by specific levels
edu_attainment_levels = byEduAtt.pivot_table(index=['Year', 'Gender'], columns='Educational Attainment', values='Percentage', aggfunc='mean').reset_index()

# Merge datasets by Year and Sex
merged_df = pd.merge(edu_attainment_levels, byYouthAge, on=['Year', 'Gender'])

# Scatter plots for visualizing the relationship between each educational attainment level and youth unemployment
educational_levels = byEduAtt['Educational Attainment'].unique()

plt.figure(figsize=(16, 12))
for idx, level in enumerate(educational_levels, 1):
    plt.subplot(3, 2, idx)
    sns.scatterplot(data=merged_df, x=level, y='Youth Unemployment', hue='Gender')
    plt.title(f'Scatter Plot: {level} vs. Youth Unemployment')
    plt.xlabel(f'{level} Percentage')
    plt.ylabel('Youth Unemployment Percentage')
    plt.grid(True)
plt.tight_layout()
plt.show()


# Clean column names in the byStates dataset
byStates.columns = byStates.columns.str.strip()

# Merge byYouthAge and byEduAttainment on Year and Gender
merged_df1 = pd.merge(byYouthAge, byEduAtt, on=['Year', 'Gender'], how='inner')

# Merge the resulting dataframe with byGender on Year and Gender
merged_df2 = pd.merge(merged_df1, byGender[['Year', 'Gender', 'Percentage']], on=['Year', 'Gender'], how='inner', suffixes=('_EduAtt', '_Gender'))

# Merge the resulting dataframe with byStates on Year
merged_df3 = pd.merge(merged_df2, byStates[['Year', 'Unemployed Person in Thousand']], on='Year', how='inner')

# Rename columns
merged_df3.rename(columns={
    'Percentage_Gender': 'Percentage Gender',
    'Youth Unemployment': 'Youth Unemployment',
    'Unemployed Person in Thousand': 'Unemployed Person in Thousand',
    'Educational Attainment': 'Educational Attainment',
    'Percentage_EduAtt': 'Percentage Educational Attainment'
}, inplace=True)

# Reorder columns
merged_df3 = merged_df3[[
    'Year',
    'Gender',
    'Percentage Gender',
    'Youth Unemployment',
    'Unemployed Person in Thousand',
    'Educational Attainment',
    'Percentage Educational Attainment'
]]

# Display the merged dataframe
merged_df3


'''
Conclusion
In conclusion, our goal is to provide a detailed understanding of youth unemployment in Malaysia and propose targeted strategies to support youth employment. By addressing the specific needs of different demographic groups and regions, we can create more inclusive and supportive opportunities for young people.

We condluded that age group, gender, states and education attainment are some of the important elements to measure in order to mitigate the youth unemployment rate

'''