import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import codecademylib3

null_outcomes = []

for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

  num_purchased = np.sum(simulated_monthly_visitors == 'y')

  null_outcomes.append(num_purchased)

#calculate the 90% interval here:
null_90CI = np.percentile(null_outcomes, [5, 95])
print(null_90CI)

# Is the observed value of 41 purchases inside or outside this interval?

# While the number of purchases in each simulated sample ranged roughly from 25 to 75 by random chance, upon further inspection of the distribution, we saw that those extreme values happened very rarely.

# By reporting an interval covering 95% of the values instead of the full range, we can say something like: “we are 90% confident that, if each visitor has a 10% chance of making a purchase, a random sample of 500 visitors will make between 37 and 63 purchases.