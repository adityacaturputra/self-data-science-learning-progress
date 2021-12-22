# This dataset contains two variables related to trunk size. The first variable, trunk_diam contains the diameter of the trunk (in inches) for each tree. The variable tree_diam_category, on the other hand, categorizes each tree based on the size of the trunk. The categories are: 'Small (0-3in)', 'Medium (3-10in)', 'Medium-Large (10-18in)', 'Large (18-24in)','Very large (>24in)'. You’ll notice that these categories are not evenly spaced with respect to diameter.

import pandas as pd
import numpy as np

# Read NYC Trees Data
nyc_trees = pd.read_csv("nyc_tree_census2.csv")

nyc_trees.tree_diam_category = pd.Categorical(nyc_trees.tree_diam_category, ['Small (0-3in)', 'Medium (3-10in)', 'Medium-Large (10-18in)', 'Large (18-24in)','Very large (>24in)'], ordered=True)

# Get Mean Diam of diameter variable, `trunk_diam`
# Calculate the mean of trunk_diam (the quantitative variable), save it as mean_diam, and print the result.
mean_diam = np.mean(nyc_trees["trunk_diam"])
print(mean_diam)

# We’ve already provided code in script.py to save tree_diam_category as an ordered categorical variable so that you can use cat.codes. Calculate the mean of tree_diam_category, save it in a variable named mean_diam_cat and print it out.
# Get Mean Category of `tree_diam_category`
mean_diam_cat = np.mean(nyc_trees["tree_diam_category"].cat.codes)
print(mean_diam_cat)
# Which category does this correspond to (remember that cat.codes translates the categories to numbers between 0 and 4)? Note how this is different from the mean you calculated in the last checkpoint. While the mean diameter is about 11.27 inches (which would be categorized as “Medium-Large”), the mean category index is about 1.97, which is between 'Medium (3-10in)' and 'Medium-Large (10-18in)'.