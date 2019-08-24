# Zara Quail August 2019 Assignment

# Calculate the mean number in each column of the BUPA Liver Disorders data set
# Reference: Ian McLoughlin. Matplotlib Pyplot video. 2018. https://web.microsoftstream.com/video/f0788c1c-c7bd-4347-98ac-477186938ed7 
import numpy

# Read data file into array.
data = numpy.genfromtxt('bupa.data', delimiter=',')

# Find the mean of the first column

firstcol = data[:,0]
meanfirstcol = numpy.mean(data[:,0])

print("Mean of first column is: ", meanfirstcol)

import matplotlib.pyplot as pl
pl.hist(firstcol)
pl.show()

