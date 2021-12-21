import scipy.stats as stats

## Checkpoint 1
# We are working in a call center, and we expect the average number of calls in our call center between 9am and 10am to be 15 calls. What is the probability that we would see exactly 15 calls in that time frame?
# calculate prob_15
prob_15 = stats.poisson.pmf(15,15)

print(prob_15)


## Checkpoint 2
# What is the probability we would get between 7 and 9 calls?
# calculate prob_7_to_9
prob_7_to_9 = stats.poisson.pmf(7,15) + stats.poisson.pmf(8,15) + stats.poisson.pmf(9,15)

print (prob_7_to_9)