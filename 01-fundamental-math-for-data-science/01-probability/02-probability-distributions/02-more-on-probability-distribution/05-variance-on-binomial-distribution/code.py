# The variance of a single coin flip will be the probability that the success happens times the probability that it does not happen: p·(1-p), or 0.5 x 0.5. Because we have n = 10 number of coin flips, the variance of a single fair coin flip is multiplied by the number of flips. Thus we get the equation:
# Variance(#ofHeads)=Var(X)=n×p×(1−p)
# Variance(#ofHeads)=10×0.5×(1−0.5)=2.5

## Checkpoint 1
# A certain basketball player has an 85% chance of making a given free throw. Uncomment variance_baskets and set it equal to the variance of free throws made from 20 shots.
variance_baskets = 20 * 15/100 * 85/100
print(variance_baskets)


## Checkpoint 2
# Let’s say a student has a 98% chance of arriving on time to class. Uncomment variance_late and set it equal to the variance of days the student will arrive late to class throughout the 180 school days in a school year.
variance_late = 98/100 * 2/100 * 180 
​
​
