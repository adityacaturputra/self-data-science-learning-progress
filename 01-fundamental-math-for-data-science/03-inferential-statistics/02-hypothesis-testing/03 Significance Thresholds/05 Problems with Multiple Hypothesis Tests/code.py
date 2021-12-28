import codecademylib3

# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Set a correct value for num_tests_50percent
# Approximately how many tests would we have to run at a 0.05 significance level so that the probability of at least one type I error would be 50%? Save your answer as the variable num_tests_50percent
num_tests_50percent = 12


# Create the plot
# Change the code to create the plot so that it shows the probability of at least one type I error for multiple tests with a significance threshold of 0.10 (instead of 0.05).
sig_threshold = 0.10
# Inspect your new plot. Now how many tests would lead to a probability of a type I error of 50%?
num_tests = np.array(range(50))
probabilities = 1-((1-sig_threshold)**num_tests)
plt.plot(num_tests, probabilities)

# Edit title and axis labels
plt.title('Type I Error Rate for Multiple Tests', fontsize=15)
# Label the y-axis
plt.ylabel('Probability of at Least One Type I Error', fontsize=12)
# Label the x-axis
plt.xlabel('Number of Tests', fontsize=12)

# Show the plot                
plt.show()