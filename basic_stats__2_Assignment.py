# -*- coding: utf-8 -*-
"""Basic Stats-2.ipynb
vyshvika 
"""

import numpy as np
import scipy.stats as stats
data = [ 1.13, 1.55, 1.43, 0.92, 1.25, 1.36, 1.32, 0.85, 1.07, 1.48,  1.20, 1.33, 1.18, 1.22, 1.29]
mean = np.mean(data)
std_dev = np.std(data, ddof=1)
n = len(data)
alpha = 0.01
t_critical = stats.t.ppf(1 - alpha/2, df=n-1)
standard_error = std_dev / np.sqrt(n)
margin_of_error = t_critical * standard_error
confidence_interval = (mean - margin_of_error, mean + margin_of_error)
print(f"Mean Durability: {mean:.2f} million characters")
print(f"Sample Standard Deviation: {std_dev:.2f} million characters")
print(f"99% Confidence Interval: {confidence_interval[0]:.2f} to {confidence_interval[1]:.2f} million characters")

import numpy as np
import scipy.stats as stats
sigma = 0.2
confidence_level = 0.99
sample_mean = 1.5
sample_size = 30
z_score = stats.norm.ppf((1 + confidence_level) / 2)
standard_error = sigma / np.sqrt(sample_size)
margin_of_error = z_score * standard_error
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
print(f"99% Confidence Interval: {confidence_interval[0]:.4f} to {confidence_interval[1]:.4f} million characters")
