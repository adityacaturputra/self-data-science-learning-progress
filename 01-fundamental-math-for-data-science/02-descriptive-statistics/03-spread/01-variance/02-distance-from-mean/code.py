import numpy as np

grades = [88, 82, 85, 84, 90]
mean = np.mean(grades)

# We’ve given you a very small dataset of five values named grades. These are five randomly chosen grades from the first teacher’s class. We’ve also calculated the mean of this small dataset and stored it in a variable named mean.

# Let’s find the difference between each of these data points and the mean. We’ve created a variable for each difference. Start with difference_one. Change the value of difference_one — it should be equal to the first value in the data set minus mean.
# Fill in the correct values for difference_two through difference_five. Some of these values will be negative! Make sure to follow the formula exactly.
# difference=X−μ

difference_one = grades[0] - mean
difference_two = grades[1] - mean
difference_three = grades[2] - mean
difference_four = grades[3] - mean
difference_five = grades[4] - mean


# IGNORE CODE BELOW HERE
print("The mean of the data set is " + str(mean) + "\n")
print("The first student is " +str(round(difference_one, 2)) + " percentage points away from the mean.")
print("The second student is " +str(round(difference_two, 2)) + " percentage points away from the mean.")
print("The third student is " +str(round(difference_three, 2)) + " percentage points away from the mean.")
print("The fourth student is " +str(round(difference_four, 2)) + " percentage points away from the mean.")
print("The fifth student is " +str(round(difference_five, 2)) + " percentage points away from the mean.")