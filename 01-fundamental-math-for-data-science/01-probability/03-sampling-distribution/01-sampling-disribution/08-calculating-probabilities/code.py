# Let’s calculate the same probability for our cod fish population.
# We know that cod have an average weight of 36 lbs with a standard deviation of 20. We want to try to fit 25 cod fish into our same crate that can hold up to 750 lbs.
# Our first step is to calculate the standard error for a sample size of 25. Using the above information, calculate the standard error and assign it to a variable called standard_error.

# Awesome! Now that we have our standard error, we can use the normal CDF to calculate the probability that a sample of 25 fish has a mean weight of 30 lbs. Using the function stats.norm.cdf(), calculate this probability and assign it to a variable cod_cdf.

# Given the probability you calculated in the last checkpoint, would you recommend trying to carry 25 cod in the crate?
# The probability of 25 fish having an average weight of 30 or less is 10%. Based on this, it’s probably a good idea to put less fish in the crate or to get a sturdier crate.

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

## Setting up our parameters
x = 750 / 25
mean = 36
std_dev = 20
samp_size = 25
standard_error = std_dev / (samp_size**.5)
cod_cdf = stats.norm.cdf(x, mean, standard_error)

print(cod_cdf)
