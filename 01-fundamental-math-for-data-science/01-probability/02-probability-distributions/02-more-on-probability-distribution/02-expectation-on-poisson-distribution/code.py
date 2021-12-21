import scipy.stats as stats
import codecademylib3

from histogram_function import histogram_function

## Checkpoint 1
# This value is very close to 15, confirming that over the 1000 observations, the expected value (or average) is 15.
# lambda = 15, 1000 random draws 
rand_vars = stats.poisson.rvs(15, size = 1000)

## Checkpoint 2
print(rand_vars.mean())


## Checkpoint 3
histogram_function(rand_vars)