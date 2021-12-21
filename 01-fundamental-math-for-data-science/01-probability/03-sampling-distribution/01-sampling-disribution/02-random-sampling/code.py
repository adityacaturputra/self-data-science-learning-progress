# In the example code, we have done the following:

# Loaded in the weights of all salmon into a dataframe called population.
# Plotted the distribution of population and calculated the mean.
# Used np.random.choice() function to generate a sample called sample of size 30 (samp_size variable is equal to 30).



# 1.
# Find the mean of the sample, round it to 3 decimal places, and assign it to a variable called sample_mean.

# 2.
# Uncomment the last 4 lines at the bottom of the editor to plot the histogram of the sample data.

# You might have to scroll down to see the 2nd plot. You can comment out the first plot’s plt.show() in order to avoid scrolling down each time.

# Run the code a couple of times. This code should behave similarly to the applet we used in the last exercise.

# 3.
# Change the sample size to 10. Does the mean change more or less each time you run it with a smaller sample size?

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import codecademylib3

population = pd.read_csv("salmon_population.csv")
population = np.array(population.Salmon_Weight)
pop_mean = round(np.mean(population),3)

## Plotting the Population Distribution
sns.histplot(population, stat='density')
plt.axvline(pop_mean,color='r',linestyle='dashed')
plt.title(f"Population Mean: {pop_mean}")
plt.show()
plt.clf() # close this plot

samp_size = 10
# Generate our random sample below
sample = np.random.choice(np.array(population), samp_size, replace = False)

### Define sample_mean below
sample_mean = round(np.mean(sample),3)

### Uncomment the lines below to plot the sample data:
sns.histplot(sample, stat='density')
plt.axvline(sample_mean,color='r',linestyle='dashed')
plt.title(F"Sample Mean: {sample_mean}")
plt.show()