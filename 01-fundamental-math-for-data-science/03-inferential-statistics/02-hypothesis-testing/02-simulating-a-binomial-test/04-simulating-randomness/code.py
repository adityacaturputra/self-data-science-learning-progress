import numpy as np
import pandas as pd

monthly_report = pd.read_csv('monthly_report.csv')

#simulate one visitor:
one_visitor = np.random.choice(['y', 'n'], size=10, p=[0.1, 0.9])
print(one_visitor)


#simulate 500 visitors:
# Do you see any visitors in this list who made a purchase?
simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])
print(np.sum(simulated_monthly_visitors == 'y'))
