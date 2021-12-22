import pandas as pd

# Get NYC Trees Data
nyc_trees = pd.read_csv("nyc_tree_census.csv")

# Using .value_counts(), calculate the proportions for each category in the health variable. The denominator for your proportions should be the number of non-missing values in the health column. Save the result to a dataframe named health_proportions and print the result.
health_proportions = nyc_trees.health.value_counts(normalize=True)
# Now, still using .value_counts(), add a parameter to include missing values in the denominator when calculating proportions for the health variable. Save the result to a dataframe named health_proportions_2. Why are the two sets of results different? Can you think of scenarios where one might be more appropriate to report than the other?
health_proportions_2 = nyc_trees.health.value_counts(dropna=False, normalize=True)

print(health_proportions)
print(health_proportions_2)



