# 1.
# You will be working with a dataset called spotify_data.csv. In script.py, use the read_csv() pandas function to load in spotify_data.csv into a variable called spotify_data.



# 2.
# Use the pandas .head() function to preview the spotify_data. If you need a reminder of how to use this function, click the hint below.



# 3.
# For this project, we are going to focus on the tempo variable. This column gives the beats per minute (bpm) of each song in spotify.csv. The other columns in our dataset are:

# danceability
# energy
# instrumentalness
# liveness
# valences
# For now, we are going to ignore these other columns.

# Create a variable called song_tempos that contains the tempo column data.



# Helper Functions
# 4.
# Let’s investigate the helper functions we will use in the following sections. A file called helper_functions.py should be opened in the workspace for you. It contains three functions: choose_statistic(), population_distribution(), and sampling_distribution(). The code in these functions is similar to what we saw in the previous lesson, but let’s explore these together.

# choose_statistic() allows us to choose a statistic we want to calculate for our sampling and population distributions. It contains two parameters:

# x: An array of numbers
# sample_stat_text: A string that tells the function which statistic to calculate on x. It takes on three values: “Mean”, “Minimum”, or “Variance”.
# population_distribution() allows us to plot the population distribution of a dataframe with one function call. It takes the following parameter:

# population_data: the dataframe being passed into the function
# sampling_distribution() allows us to plot a simulated sampling distribution of a statistic. The simulated sampling distribution is created by taking random samples of some size, calculating a particular statistic, and plotting a histogram of those sample statistics. It contains three parameters:

# population_data: the dataframe being sampled from
# samp_size: the size of each sample
# stat: the specific statistic being measured for each sample — either “Mean”, “Minimum”, or “Variance”
# Read through these functions in helper_function.py to familiarize yourself with them. Click the hint to see examples of population_distribution() and sampling_distribution() being used.



# Sampling Distribution Exploration
# 5.
# Now that our data is loaded into script.py and we have gone over the functions in helper_functions.py let’s start our sampling distributions exploration. Make sure to write your code in script.py.

# To start off, let’s use the population_distribution() function to graph distribution of song_tempos.

# When you click run, you should see a graph with the following title:

# Population Distribution
# How would you describe this distribution?



# 6.
# Now let’s plot the sampling distribution of the sample mean with sample sizes of 30 songs. To do this, use the sampling_distribution() helper function.

# Once you hit run, you should see a graph with the following title:

# Sampling Distribution of the Mean
# Mean of the Sample Means: {Mean of the Sample Means} 
# Population Mean: {Population Mean}


# 7.
# Compare your sampling distribution of the sample means to the population mean. Is the sample mean an unbiased or biased estimator of the population?



# 8.
# Now let’s plot the sampling distribution of the sample minimum with sample sizes of 30 songs. To do this, use the sampling_distribution() helper function.

# Once you hit run, you should see a graph with the following title:

# Sampling Distribution of the Minimum
# Mean of the Sample Minimums: {Mean of the Sample Minimums}
# Population Mean: {Population Mean}


# 9.
# Compare your sampling distribution of the sample minimums to the population minimum. Is the sample minimum an unbiased or biased estimator of the population?



# 10.
# Now let’s plot the sampling distribution of the sample variance with sample sizes of 30 songs. To do this, use the sampling_distribution() helper function.

# Once you hit run, you should see a graph with the following title:

# Sampling Distribution of the Variance
# Mean of the Sample Variances: {Mean of the Sample Variances}
# Population Variance: {Population Variance}


# 11.
# Compare your sampling distribution of the sample variance to the population variance. Does the sample variance appear to be an unbiased or biased estimator of the population?

# Click the hint for more information about sample variance.



# 12.
# Go to line 17 in helper_functions.py. You should see the following line of code:

# np.var(x)
# Change this to:

# np.var(x, ddof=1)
# Adding this ddof=1 parameter will divide our input by n-1 instead of n, therefore applying the sample variance formula.

# After changing this line of code, run script.py. Does the sample variance appear to be an unbiased or biased estimator of the population?



# Calculating Probabilities
# 13.
# We have a good sense of some sample statistics now that we’ve investigated sampling distributions. Let’s take our analysis further by calculating probabilities.

# First, calculate the population mean and population standard deviation of song_tempos. Save these values in two separate variables called population_mean and population_std.



# 14.
# Use population_mean and population_std to calculate the standard error of the sampling distribution of the sample mean with a sample size of 30.

# Save this value in a variable called sampling_standard_deviation.



# 15.
# You are afraid that if the average tempo of the songs you randomly select is less than 140bpm that your party will not be enjoyable.

# Using population_mean and standard_error in a CDF, calculate the probability that the sample mean of 30 selected songs is less than 140bpm.

# Remember to print your result into the output terminal.



# 16.
# You know the party will be truly epic if the randomly sampled songs have an average tempo of greater than 150bpm.

# Using population_mean and standard_error in a CDF, calculate the probability that the sample mean of 30 selected songs is GREATER than 150bpm.

# Remember to print your result into the output terminal.

# Does this probability make you feel confident about the party?



# Extras
# 17.
# Awesome job! You are ready to throw an awesome party! If you want to do some more exploration of sampling distributions, here are some more opportunities:

# Add another sample statistic to the choose_statistic() function in helper_functions.py — such as median, mode, or maximum.
# Explore a different column of data from the spotify_data.csv dataset.
# Use the sampling distribution of the sample minimum to estimate the probability of observing a specific sample minimum. For example, from the plot, what is the chance of getting a sample minimum that is less than 130bpm?



from helper_functions import choose_statistic, population_distribution, sampling_distribution
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import codecademylib3

# task 1: load in the spotify dataset
spotify_data = pd.read_csv("spotify_data.csv")

# task 2: preview the dataset
print(spotify_data.head())

# task 3: select the relevant column
song_tempos = spotify_data['tempo']

# task 5: plot the population distribution with the mean labeled
population_distribution(song_tempos)

# task 6: sampling distribution of the sample mean
sampling_distribution(song_tempos, 30, "Mean")

# task 8: sampling distribution of the sample minimum
sampling_distribution(song_tempos, 30, "Minimum")

# task 10: sampling distribution of the sample variance
sampling_distribution(song_tempos, 30, "Variance")

# task 13: calculate the population mean and standard deviation
population_mean = np.mean(song_tempos)
population_std = np.std(song_tempos)

# task 14: calculate the standard error
standard_error = population_std/(30**.5)

# task 15: calculate the probability of observing an average tempo of 140bpm or lower from a sample of 30 songs
print(stats.norm.cdf(140, population_mean, standard_error))

# task 16: calculate the probability of observing an average tempo of 150bpm or higher from a sample of 30 songs
print(1-stats.norm.cdf(150, population_mean, standard_error))

# EXTRA
