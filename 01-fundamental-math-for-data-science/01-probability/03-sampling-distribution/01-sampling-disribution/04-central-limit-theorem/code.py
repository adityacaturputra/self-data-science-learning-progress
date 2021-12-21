import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import codecademylib3

cod_population = pd.read_csv("cod_population.csv")
# Save transaction times to a separate numpy array
population = cod_population['Cod_Weight']

## Checkpoint 1:
# In order to see the Central Limit Theorem in action, let’s look at another population of fish that is not normally distributed.
# We have loaded this data on the weight of cod fish into the workspace.
# Uncomment the three lines underneath ## Checkpoint 1 to see the plot of the distribution of cod fish. Note the distribution.
sns.histplot(population, stat = 'density' )
plt.title("Population Distribution")
plt.show()
# The distribution is not normal (which would look like a bell curve). It is highly skewed right.

sample_means = []

# Below is our sample size
samp_size = 50

for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    this_sample_mean = np.mean(samp)
    sample_means.append(this_sample_mean)

## Checkpoint 2
# Now that we have seen the skewed population distribution, let’s simulate a sampling distribution of the mean. According to the CLT, we will see a normal distribution once the sampling size is large enough. To start, we have set the sample size to 6.
# Uncomment the five lines at the very bottom, run the code once, and take a look at the sampling distribution.
# Remember to scroll down to see the second plot.
# With such a small sample size, the sampling distribution looks slightly skewed. This is because the population was not normally distributed and we have a small sample size.
plt.clf() # this closes the previous plot
sns.histplot(sample_means, stat = 'density' )
plt.title("Sampling Distribution of the Mean")
plt.xlabel("Weight (lbs)")
# Now change the sample size to 50 and run the code. Does the estimated sampling distribution look more normal now?
plt.show()
# Change the variable named samp_size to 50. Now that we have increased the sample size, the sampling distribution should look more normal.