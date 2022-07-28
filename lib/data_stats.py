"""
Takes a list or a tuple and returs basic statistics in a dictionary
jornamon 2022
"""


import math

def data_stats(data):

    num_samples = len(data)

    sums = 0
    for i in range(num_samples):
        sums += data[i]
    mean = sums / num_samples

    diff_squared = 0
    for i in range(num_samples):
        diff_squared += (data[i] - mean) ** 2

    stdev = math.sqrt(diff_squared / (num_samples - 1))
    smax = max(data)
    smin = min(data)
    
    return {'num_samples': num_samples, 'min': smin, 'max': smax, 'avg': mean, 'stdev': stdev,
             'range': smax - smin, 'ovh': (mean - smin)/smin * 100}
