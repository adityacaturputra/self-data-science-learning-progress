# Import packages
import codecademylib
import numpy as np
import pandas as pd

# Import matplotlib pyplot
from matplotlib import pyplot as plt

# Read in transactions data
greatest_books = pd.read_csv("top-hundred-books.csv")

# Save transaction times to a separate numpy array
author_ages = greatest_books['Ages']

# Use numpy to calculate the average age of the top 100 authors
average_age = np.average(author_ages)

median_age = np.median(author_ages)

# Plot the figure
plt.hist(author_ages, range=(10, 80), bins=14,  edgecolor='black')
plt.title("Age of Top 100 Novel Authors at Publication")
plt.xlabel("Publication Age")
plt.ylabel("Count")
plt.axvline(average_age, color='r', linestyle='solid', linewidth=2, label="Mean")
plt.axvline(median_age, color='y', linestyle='solid', linewidth=2, label="Median")
plt.legend()

plt.show()

# Discussion
# Take a look at the histogram to the right. It displays the author age distribution with vertical lines for the mean (red) and median (yellow).

# Do you feel like the median of our dataset, 40.5, provides us enough information to claim when authors publish their greatest work?

# We argue it does not.

# Although the median is a good measure of the dataset’s center, we cannot make a definitive claim about when authors publish their greatest work — the youngest author published at 18 and the oldest at 76. It would be irresponsible to say anything but, “it seems to be possible at almost any age.”

# Notice that the mean and the median are nearly equal. This is not a surprising result, as both statistics are a measure of the dataset’s center. However, it’s worth noting that these results will not always be so close.

# In the instructions below, we’ve written a brief explanation that puts median in the context of our problem.

# The median age of authors, when they publish their best work, from Le Monde’s 100 greatest books is 41.

# While this does not tell us much about which year is an author’s greatest year, it does indicate that half of the authors from the survey find their greatest success before the age of 41 and half find their greatest success after the age of 41.