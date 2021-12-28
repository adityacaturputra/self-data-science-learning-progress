import numpy as np
import pandas as pd
import codecademylib3

monthly_report = pd.read_csv('monthly_report.csv')


# Each row of the dataset monthly_report represents a single visitor to Live-it-LIVE.com during the week in question. Use .head() to print the first five rows of the data once again and inspect the 'purchase' column. What are the values and how can you tell whether someone made a purchase?
#print the head of monthly_report:
print(monthly_report.head())

# Calculate the sample size and assign it to a variable named sample_size. Print sample_size. How many visitors accessed the website this week?
#calculate and print sample_size:
sample_size = len(monthly_report)
print(sample_size)

# Calculate the number of visitors who made a purchase this week and save it to a variable named num_purchased. Print num_purchased. How many visitors made a purchase this week?
#calculate and print num_purchased:
num_purchased = np.sum(monthly_report.purchase == 'y')
print(num_purchased)