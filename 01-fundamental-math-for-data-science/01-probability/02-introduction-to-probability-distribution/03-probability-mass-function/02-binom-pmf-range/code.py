import scipy.stats as stats

## Checkpoint 1 : probability of observing between 4 to 6 heads from 10 coin flips.
prob_1 = stats.binom.pmf(4, 10, 0.5) + stats.binom.pmf(5, 10, 0.5) +  stats.binom.pmf(6, 10, 0.5)
print(prob_1)

## Checkpoint 2 : probability of observing more than 2 heads from 10 coin flips.
prob_2 = 1 - (stats.binom.pmf(1, 10, 0.5) +  stats.binom.pmf(2, 10, 0.5) + stats.binom.pmf(0, 10, 0.5))
print(prob_2)