# In the workspace, we’ve set up a simulation of a population that has a mean of 10 and a standard deviation of 10. We’ve set a sample size of 50.
# According to the CLT, we should have a sampling distribution of the mean that is normally distributed and has a mean that is close to the population mean.
# Run the code once. Does what you see align with the CLT?
# Yes, what we are seeing aligns with the CLT. The sampling distribution of the mean looks like a bell curve and has a mean close to the population mean.

# Set variable samp_size equal to 6 and run the code.
# Why do you think the CLT applies here, even with a smaller sample size?
# Because the original population is normally distributed, the CLT applies even with a smaller sample size.

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns
import codecademylib3

# Set the population mean & standard deviation:
population_mean = 10
population_std_dev = 10
# Set the sample size:
samp_size = 6

# Create the population
population = np.random.normal(population_mean, population_std_dev, size = 100000)

# Simulate the samples and calculate the sampling distribution
sample_means = []
for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    sample_means.append(np.mean(samp))

mean_sampling_distribution = round(np.mean(sample_means),3)

# Plot the original population
sns.histplot(population, stat = 'density')
plt.title(f"Population Mean: {population_mean} ")
plt.xlabel("")
plt.show()
plt.clf()

## Plot the sampling distribution
sns.histplot(sample_means, stat='density')
# calculate the mean and SE for the probability distribution
mu = np.mean(population)
sigma = np.std(population)/(samp_size**.5)
# plot the normal distribution with mu=popmean, sd=sd(pop)/sqrt(samp_size) on top
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)

plt.plot(x, stats.norm.pdf(x, mu, sigma), color='k', label = 'normal PDF')
plt.title(f"Sampling Dist Mean: {mean_sampling_distribution}")
plt.xlabel("")
plt.show()