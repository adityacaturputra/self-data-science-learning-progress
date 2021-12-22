import pandas as pd

# Read NYC Trees data
nyc_trees = pd.read_csv("./nyc_tree_census.csv")

# Calculate a table of proportions for the status column. Save this table of proportions as tree_status_proportions and print the result.
tree_status_proportions = nyc_trees["status"].value_counts(normalize = True)

print(tree_status_proportions)
