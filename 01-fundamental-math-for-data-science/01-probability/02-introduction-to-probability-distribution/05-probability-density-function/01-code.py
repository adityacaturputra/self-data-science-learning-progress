# the probability that a randomly chosen woman is less than 175 cm tall.
import scipy.stats as stats

# x: the value of interest
# loc: the mean of the probability distribution
# scale: the standard deviation of the probability distribution

prob = stats.norm.cdf(175, 167.64, 8)
print(prob)