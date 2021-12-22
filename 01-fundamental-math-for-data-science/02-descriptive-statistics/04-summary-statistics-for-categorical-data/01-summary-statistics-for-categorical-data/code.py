# As a final exercise, a new dataset has been loaded for you in the workspace. Follow the instructions below to inspect and summarize the categorical variables in this data.

# film_permits contains a sample of NYC filming permits. Inspect the first few rows. Think about how you might explore and summarize this data. Some exercises you might wish to work through:

# Which variables in this data are nominal? Which are ordinal?
# Which Boroughs are granted permits for the most TV pilot episodes?
# Summarize the types (Category) and subtypes (SubCategoryName) of projects that get filming permits granted.

import pandas as pd
import codecademylib3

# Read CSV
film_permits = pd.read_csv('film_permits.csv')

# Look first few rows
print(film_permits.head()) 

# Nominal Vars
nominalvars = ['EventType', 'Borough', 'Category', 'SubCategoryName']

# Ordinal Vars - We might consider an Id like 'EventID' an ordinal variable in some situations

# Borough with the most permits for pilot episodes
print(film_permits[film_permits.SubCategoryName == 'Pilot'].Borough.value_counts())

# Summarize the Top Categories
print(film_permits.Category.value_counts())

# Summarize the Top Subcategories
print(film_permits.SubCategoryName.value_counts())
