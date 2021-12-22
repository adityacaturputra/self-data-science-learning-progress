# In this project, you will find the mean, median, and mode cost of one-bedroom apartments in three of the five New York City boroughs: Brooklyn, Manhattan, and Queens.

# Using your findings, you will make conclusions about the cost of living in each of the boroughs. We will also discuss an important assumption that we make when we point out differences between the boroughs.

# We worked with Streeteasy.com to collect this data. While we will only focus on the cost of one-bedroom apartments, the dataset includes a lot more information if you’re interested in asking your own questions about the Brooklyn, Manhattan, and Queens housing market.

# Import packages
import numpy as np
import pandas as pd
from scipy import stats

# Read in housing data
brooklyn_one_bed = pd.read_csv('brooklyn-one-bed.csv')
brooklyn_price = brooklyn_one_bed['rent']

manhattan_one_bed = pd.read_csv('manhattan-one-bed.csv')
manhattan_price = manhattan_one_bed['rent']

queens_one_bed = pd.read_csv('queens-one-bed.csv')
queens_price = queens_one_bed['rent']

# Add mean calculations below 
brooklyn_mean = np.mean(brooklyn_price)
manhattan_mean = np.mean(manhattan_price)
queens_mean = np.mean(queens_price)



# Add median calculations below
brooklyn_median = np.median(brooklyn_price)
manhattan_median = np.median(manhattan_price)
queens_median = np.median(queens_price)



# Add mode calculations below
brooklyn_mode = stats.mode(brooklyn_price)
manhattan_mode = stats.mode(manhattan_price)
queens_mode = stats.mode(queens_price)








##############################################
##############################################
##############################################







# Don't look below here
# Mean
try:
    print("The mean price in Brooklyn is " + str(round(brooklyn_mean, 2)))
except NameError:
    print("The mean price in Brooklyn is not yet defined.")
try:
    print("The mean price in Manhattan is " + str(round(manhattan_mean, 2)))
except NameError:
    print("The mean in Manhattan is not yet defined.")
try:
    print("The mean price in Queens is " + str(round(queens_mean, 2)))
except NameError:
    print("The mean price in Queens is not yet defined.")
    
    
# Median
try:
    print("The median price in Brooklyn is " + str(brooklyn_median))
except NameError:
    print("The median price in Brooklyn is not yet defined.")
try:
    print("The median price in Manhattan is " + str(manhattan_median))
except NameError:
    print("The median price in Manhattan is not yet defined.")
try:
    print("The median price in Queens is " + str(queens_median))
except NameError:
    print("The median price in Queens is not yet defined.")
    
    
#Mode
try:
    print("The mode price in Brooklyn is " + str(brooklyn_mode[0][0]) + " and it appears " + str(brooklyn_mode[1][0]) + " times out of " + str(len(brooklyn_price)))
except NameError:
    print("The mode price in Brooklyn is not yet defined.")
try:
    print("The mode price in Manhattan is " + str(manhattan_mode[0][0]) + " and it appears " + str(manhattan_mode[1][0]) + " times out of " + str(len(manhattan_price)))
except NameError:
    print("The mode price in Manhattan is not yet defined.")
try:
    print("The mode price in Queens is " + str(queens_mode[0][0]) + " and it appears " + str(queens_mode[1][0]) + " times out of " + str(len(queens_price)))
except NameError:
    print("The mode price in Queens is not yet defined.")






# What does our data tell us?
# 11.
# Now what?

# We don’t find the mean, median, and mode of a dataset for the sake of it.

# The point is to make inferences from our data. What can you say about the housing prices in Brooklyn, Queens, and Manhattan? Besides, “It’s really expensive to live in any of them.”

# Take a minute to think through it. We added our thoughts to the hint.


# It looks like the average cost of one-bedroom apartments in Manhattan is the most, and in Queens is the least. This pattern holds for the median and mode values as well.

# While the mode is not the most important indicator of centrality, the fact that mean, median, and mode are within a few hundred dollars for each borough indicates the data is centered around:

# $3,300 for Brooklyn
# $3,900 for Manhattan
# $2,300 for Queens
# 12.
# Did you make any assumptions when you drew inferences in the previous task?

# If so, what assumptions did you make? We added our thoughts to the hint.


# We assumed that the data from Streeteasy is representative of housing prices for the entire borough. Given that Streeteasy is only used by a subset of property owners, this is not a fair assumption. A quick search on rentcafe.com will tell you the averages are more like:

# $2,695 for Brooklyn one-bedroom apartments
# $4,188 for Manhattan one-bedroom apartments
# $2,178 for Queens one-bedroom apartments
# This is an interesting finding. Why may the cost from rentcafe.com be higher in Manhattan than in Brooklyn or Queens?

# Although we don’t have the answer to this question, it’s worth thinking about the possible differences between our Streeteasy data and where rentcafe is pulling their data.

# 13.
# Finally, think about what the histogram for each dataset will look like.

# If you have the time, take a minute to make a rough sketch of the histograms for the cost of a one-bedroom apartment in Brooklyn, Manhattan, and Queens.