import scipy.stats as stats

## Checkpoint 1
# Working at a call center where the average number of calls between 9am and 10am is 15 calls, what is the probability of observing more than 20 calls?
# calculate prob_more_than_20
prob_more_than_20 = 1 - stats.poisson.cdf(20, 15)

print(prob_more_than_20)

## Checkpoint 2
# What is the probability of observing between 17 to 21 calls when the expected number of calls is 15?
# calculate prob_17_to_21
prob_17_to_21 = stats.poisson.cdf(21, 15) - stats.poisson.cdf(16, 15)

print (prob_17_to_21)
