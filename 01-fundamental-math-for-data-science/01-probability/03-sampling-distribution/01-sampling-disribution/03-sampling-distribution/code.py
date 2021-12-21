# Let’s estimate the sampling distribution of the mean using a population of cod fish. As we did with salmon fish, we will pretend we are all-knowing and have captured weight data on every cod fish in the ocean. In the workspace, we’ve loaded in the cod weight data.

# We’ve set the sample size equal to 50 and created a for loop to take 500 random samples.

# Inside the for loop, use the function np.mean() to calculate the mean of each sample. Save this to a variable called this_sample_mean.
# Then, still inside the for loop, append this_sample_mean to the list sample_means and run the simulation.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import codecademylib3

population = pd.read_csv("cod_population.csv")
# Save transaction times to a separate numpy array
population = population['Cod_Weight']

sample_size = 50
sample_means = []

for i in range(500):
  samp = np.random.choice(population, sample_size, replace = False)
  # calculate mean here
  this_sample_mean = np.mean(samp)
  # append here
  sample_means.append(this_sample_mean)

sns.histplot(sample_means,stat='density')
plt.title("Sampling Distribution of the Mean")
plt.xlabel("Weight (lbs)")
plt.show()