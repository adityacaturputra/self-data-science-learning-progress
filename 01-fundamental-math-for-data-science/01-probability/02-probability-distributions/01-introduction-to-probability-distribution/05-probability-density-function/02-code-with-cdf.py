# x: the value of interest
# loc: the mean of the probability distribution
# scale: the standard deviation of the probability distribution

# the probability of randomly observing a woman between 165 cm to 175 cm, assuming heights still follow the Normal(167.74, 8) distribution.
import scipy.stats as stats
# P(165 < X < 175) = P(X < 175) - P(X < 165)
# stats.norm.cdf(x, loc, scale) - stats.norm.cdf(x, loc, scale)
print(stats.norm.cdf(175, 167.74, 8) - stats.norm.cdf(165, 167.74, 8))


# probability of observing a woman taller than 172 centimeters, assuming heights still follow the Normal(167.74, 8) distribution. We can think of this as the opposite of observing a woman shorter than 172 centimeters.
# P(X > 172) = 1 - P(X < 172)
# 1 - stats.norm.cdf(x, loc, scale)
print(1 - stats.norm.cdf(172, 167.74, 8))