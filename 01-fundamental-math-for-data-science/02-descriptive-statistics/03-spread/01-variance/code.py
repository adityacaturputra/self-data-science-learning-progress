# You might be wondering why we need to compute the variance. After all, by comparing histograms, it was fairly easy to tell which dataset had a larger spread.

# Variance is useful because it is a measure of spread. While we might get a general understanding of the spread by looking at a histogram, computing the variance gives us a numerical value that helps us describe the level of confidence of our comparison.

# It is also interesting to consider datasets that don’t have the same general curve.

# Run the code to see two datasets that have a similar mean, but look very different. You’ll also see a printout of their mean and variance. Before looking at the printout, try to guess which dataset has a larger variance.

# Checkpoint 2 Passed

# Hint
# Dataset two is a bimodal distribution — there are two distinct peaks. In this case, the variance of the bimodal dataset is slightly larger because fewer datapoints are centered around the mean.

import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
from data import dataset_one, dataset_two

plt.hist(dataset_one, alpha =0.75, label = "dataset_one", bins = 80)
plt.hist(dataset_two, alpha = 0.5, label = "dataset_two", bins = 80)
plt.legend()

print("The mean of the first dataset is " + str(np.mean(dataset_one)))
print("The mean of the second dataset is " + str(np.mean(dataset_two)) + "\n")

print("The variance of the first dataset is " + str(np.var(dataset_one)))
print("The variance of the second dataset is " + str(np.var(dataset_two)))

plt.show()
