# In the workspace, you can see a population distribution and a sampling distribution (scroll down to see the sampling distribution). Right now, the sample size is set to 10.
# Increase the sample size to 50 and note the change in the shape of the sampling distribution.
# A smaller standard error means that the distribution will be taller & skinnier. Is that the case?

# Now increase the standard deviation of the population to 30.
# This means that the population distribution will have more variation (and will therefore appear wider and flatter). The sampling distribution will also become wider and flatter because the standard error will increase (due to the larger numerator).
# Does what you see line up with what you expect?

# Play around with the two variables samp_size and population_std_dev some more.
# Keep in mind that:
# As sample size increases, the standard error will decrease.
# As the population standard deviation increases, so will the standard error.


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import codecademylib3

population_mean = 36
population_std_dev = 30
# Set the sample size:
samp_size = 50

### Below is code to create simulated dataset and calculate Standard Error

# Create the population
population = np.random.normal(population_mean, population_std_dev, size = 100000)

## Simulate the sampling distribution
sample_means = []
for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    sample_means.append(np.mean(samp))

mean_sampling_distribution = round(np.mean(sample_means),3)
std_sampling_distribution = round(np.std(sample_means),3)

std_error = population_std_dev / (samp_size **0.5)

sns.histplot(population, stat = 'density')
plt.title(f"Population Mean: {population_mean} \n Population Std Dev: {population_std_dev} \n Standard Error = {population_std_dev} / sq rt({samp_size}) \n Standard Error = {std_error} ")
plt.xlim(-50,125)
plt.ylim(0,0.045)
plt.show()
plt.clf()

## Plot the sampling distribution
sns.histplot(sample_means, stat = 'density')
# calculate the mean and SE for the probability distribution
mu = np.mean(population)
sigma = np.std(population)/(samp_size**.5)

# plot the normal distribution with mu=popmean, sd=sd(pop)/sqrt(samp_size) on top
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma), color='k', label = 'normal PDF')
# plt.axvline(mean_sampling_distribution,color='r',linestyle='dashed')
plt.title(f"Sampling Dist Mean: {mean_sampling_distribution} \n Sampling Dist Standard Deviation: {std_sampling_distribution}")
plt.xlim(20,50)
plt.ylim(0,0.3)
plt.show()