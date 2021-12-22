import pandas as pd
import numpy as np

# Read NYC trees data
nyc_trees = pd.read_csv("./nyc_tree_census.csv")
# Using the NYC trees dataset, find the unique values in the column health. Save the unique categories to a variable named tree_health_statuses and print the result.
tree_health_statuses = nyc_trees["health"].unique()
print(tree_health_statuses)
# Create a list named health_categories which lists the categories from worst to best. You should exclude NaN values from your list.
health_categories = ['Poor', 'Fair', 'Good']
# Using the health_categories list you created in the previous exercise, convert health in the original dataset to a categorical variable type ('category').
nyc_trees["health"] = pd.Categorical(nyc_trees["health"], health_categories, ordered=True)
# Using cat.codes, calculate the value that corresponds to the median value of health. Save it as a variable named median_health_status and print the result.
median_index = np.median(nyc_trees["health"].cat.codes)
median_health_status = health_categories[int(median_index)]
print(median_health_status) 