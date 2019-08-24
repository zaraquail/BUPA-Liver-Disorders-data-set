# Zara Quail August 2019 Assignment

# Calculate the mean number in each column of the BUPA Liver Disorders data set
# Reference: Ian McLoughlin. Matplotlib Pyplot video. 2018. https://web.microsoftstream.com/video/f0788c1c-c7bd-4347-98ac-477186938ed7 
# Column 1

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

# Column 2 (alkphos)

# Find the mean of the second column

secondcol = data[:,1]
meansecondcol = numpy.mean(data[:,1])

print("Mean of second column is: ", meansecondcol)

import matplotlib.pyplot as pl
pl.hist(secondcol)
pl.show()

# Column 3 (sgpt)

# Find the mean of the third column

thirdcol = data[:,2]
meanthirdcol = numpy.mean(data[:,2])

print("Mean of third column is: ", meanthirdcol)

import matplotlib.pyplot as pl
pl.hist(thirdcol)
pl.show()

# Column 4 (sgot)

# Find the mean of the fourth column

fourthcol = data[:,3]
meanfourthcol = numpy.mean(data[:,3])

print("Mean of fourth column is: ", meanfourthcol)

import matplotlib.pyplot as pl
pl.hist(fourthcol)
pl.show()

# Column 5 (gammagt)

# Find the mean of the fifth column

fifthcol = data[:,4]
meanfifthcol = numpy.mean(data[:,4])

print("Mean of fifth column is: ", meanfifthcol)

import matplotlib.pyplot as pl
pl.hist(fifthcol)
pl.show()

# Column 6 (drinks)

# Find the mean of the sixth column

sixthcol = data[:,5]
meanfifthcol = numpy.mean(data[:,5])

print("Mean of sixth column is: ", meansixthcol)

import matplotlib.pyplot as pl
pl.hist(sixthcol)
pl.show()