import pandas as pd
import numpy as np

# Get NYC Trees Data
nyc_trees = pd.read_csv('nyc_tree_census.csv')

# Find the frequency and proportion of trees that were recorded as Alive. You can do this by transforming the status variable to an indicator for if a tree is alive (indicated by status == 'Alive') or not. Save the results to variables named living_frequency and living_proportion and print them to the console
living_frequency = (nyc_trees.status == 'Alive').sum()
living_proportion = (nyc_trees.status == 'Alive').mean()
print(living_frequency)
print(living_proportion)

# Find the frequency and proportion of trees with trunk_diam > 30. Save the results to variables named giant_frequency and giant_proportion and print them to the console.
giant_frequency = (nyc_trees.trunk_diam > 30).sum()
giant_proportion = (nyc_trees.trunk_diam > 30).mean()
print(giant_frequency)
print(giant_proportion)
