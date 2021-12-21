import scipy.stats as stats
import numpy as np

## Checkpoint 1
# At the end of the year, your company’s boss decides that the end-of-year bonus will be 8% of each employee’s salary. If the average salary in the company is $75,000, what is the expected value (or average value) of the bonuses?
expected_bonus = 75000 * 8/100
print(expected_bonus)


## Checkpoint 2
# Let’s say that the number of goals a soccer team scores follows the Poisson distribution with lambda equal to four. Uncomment num_goals and set it equal to the expected number of goals scored in 100 games.
# Use the stats.poisson.rvs() method from the scipy library with lambda equal to four and 100 random draws.
num_goals = stats.poisson.rvs(4, size = 100)



## Checkpoint 3
# Print the variance of num_goals using np.var().
print(np.var(num_goals))


## Checkpoint 4
# Someone thinks that the soccer team is being robbed of goals each game and decides that they are going to count each goal from this team as 2 goals.
# Calculate and print the variance of num_goals_2 to see that the variance of num_goals_2 is equal to the variance of num_goals times two squared (same as times four).
num_goals_2 = num_goals * 2
print(np.var(num_goals_2))