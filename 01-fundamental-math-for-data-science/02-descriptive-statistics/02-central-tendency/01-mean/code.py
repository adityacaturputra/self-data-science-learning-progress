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

print("The average age of the 100 greatest authors, according to Le Monde is: " + str(average_age))

# Plot the figure
plt.hist(author_ages, range=(10, 80), bins=14,  edgecolor='black')
plt.title("Age of Top 100 Novel Authors at Publication")
plt.xlabel("Publication Age")
plt.ylabel("Count")
plt.axvline(average_age, color='r', linestyle='solid', linewidth=2, label="Mean")
plt.legend()

plt.show()



# Circling back to the original question, do you feel like the average of our dataset, 42.12, provides us enough information to claim when someone is their most creative and productive?

# Take a look at the histogram and mean (in red) to the right as you consider this question.

# We would say, No. Though we could argue against its use for a few reasons, below, we’ve highlighted two:

# The date of publication is not necessarily an author’s most creative year. When did they start authoring the book? What factors impacted their writing during those years?
# The average age of the publishing dates for 100 authors may not accurately measure peak creativity in other professions. The average age of painters or sculptors may be very different.
# So, what kind of information does the average provide us, and why would we use the average to describe something when we could display a histogram?

# The most important outcome is that we’re able to use a single number as a measure of centrality. Although histograms provide more information, they are not a concise or precise measure of centrality — the reader must interpret it for themselves.

# Instructions
# Take a look at the histogram to the right. Are you older or younger than the average age at publication?

# While this doesn’t tell you much about when someone, maybe you, will have their most creative year. However, this type of data could be used as an example in a broader study on aging.