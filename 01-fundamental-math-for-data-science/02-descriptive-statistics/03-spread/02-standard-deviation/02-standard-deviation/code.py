# We’ve written some code that calculates the variance of the NBA dataset and the OkCupid dataset.

# The variances are stored in variables named nba_variance and okcupid_variance.

import numpy as np
from data import nba_data, okcupid_data

nba_variance = np.var(nba_data)
okcupid_variance = np.var(okcupid_data)

#Change these variables to be the standard deviation of each dataset.
nba_standard_deviation = nba_variance ** 0.5
okcupid_standard_deviation = okcupid_variance ** 0.5

#IGNORE CODE BELOW HERE
print("The standard deviation of the NBA dataset is " +str(nba_standard_deviation))
print("The standard deviation of the OkCupid dataset is " + str(okcupid_standard_deviation))