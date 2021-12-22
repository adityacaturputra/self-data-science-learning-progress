# Import packages
import codecademylib
import numpy as np
import pandas as pd
from scipy import stats

# Import matplotlib pyplot
from matplotlib import pyplot as plt

# Read in transactions data
greatest_books = pd.read_csv("top-hundred-books.csv")

# Save transaction times to a separate numpy array
author_ages = greatest_books['Ages']

# Calculate the average and median value of the author_ages array
average_age = np.average(author_ages)
median_age = np.median(author_ages)
mode_age = stats.mode(author_ages).mode

# Plot the figure
plt.hist(author_ages, range=(10, 80), bins=14,  edgecolor='black')
plt.title("Author Ages at Publication")
plt.xlabel("Publication Age")
plt.ylabel("Count")
plt.axvline(average_age, color='r', linestyle='solid', linewidth=3, label="Mean")
plt.axvline(median_age, color='y', linestyle='dotted', linewidth=3, label="Median")
plt.axvline(mode_age, color='orange', linestyle='dashed', linewidth=3, label="Mode")
plt.legend()

plt.show()


# In this lesson, you found that 38 was the most common age, at publication, for an author from the Le Monde survey. How does this number compare to your guess from the beginning of the lesson?

# The mode is close to the median and mean of the dataset, but it is not in the tallest bucket. This should not be surprising, as the histogram indicates the data is centered between the ages of 30 and 50 — there is a higher chance of a mode in that range than outside of it.

# The mode is not always this close to the median and mean, and often will not be in the tallest bucket.

# Look at the 25-30 year-old bin. There are nine observations in it. If all the values in that bin happened to be 27, then the dataset’s mode would be 27. Although unlikely, it is possible. Below, we show what this would look like:

# Mode set to 27

# Based on this graph, it is fair to say the mode may not always be a great measure of where the data is centered. Simply put, mode is a measure of the most frequent observation in the dataset, and is not an indication of the tallest bin in a histogram.

# In the instructions below, we’ve written a brief explanation that puts mode in the context of our problem.

# Instructions
# The most common age of an author from Le Monde’s 100 greatest books, when they publish their best work, is 38.