# BUPA-Liver-Disorders-data-set August 2019 Programming and Scripting Project

## Higher Diploma in Data Analytics Course, Galway Mayo Institute of Technology

## Zara Quail 

### BUPA Liver Disorders Data Set Summary

The BUPA Liver Disorders data set was created by BUPA Medical Research Limited and was donated to the UCI Machine Learning Repository by Richard S. Forsyth in May 1990.[1] The data set is multivariate and includes categorical, integer and real attributes.[1] Each line of the data records  7 variables from one of a total of 345 male individuals.[1] The variables represented include the results of 5 blood tests that are considered potentially indicative of liver disorders that are caused by drinking excess alcohol.[1] The blood test results are the first 5 variables and include: 1) mean corpuscular volume (MCV), 2) alkaline phosphatase (alk phos), 3) alanine aminotransferase (sgpt), 4) aspartate aminotransferase (sgot), 5) gamma-glutamyl transpeptidase (gamma gt). The sixth variable is the number of half-pint equivalents of alcoholic beverages drunk per day (drinks) and the seventh variable is the selector field created by the BUPA researchers to split the data into train/test sets.[1] The data set would be considered to be complete as there are no missing values. [1] It is noted that the data set does not present any variables that denote the presence or absence of a liver disorder for each of the individuals.[1] The data set has often been utilised as a benchmark dataset.[2] However,  as noted by authors McDermott and Forsyth in 2016, the last variable of the data set has been incorrectly interpreted by some as a classification label, rather than the test/train indicator, resulting in useless results and potentially dangerous and incorrect assignment of a liver disease to an individual.[2] In addition, duplicates have been noted in the following data set rows:[1]

row 84 and 86:   94,58,21,18,26,2.0,2

row 141 and 318:   92,80,10,26,20,6.0,1

row 143 and 150:   91,63,25,26,15,6.0,1

row 170 and 176:   97,71,29,22,52,8.0,1

### Downloading the Data set

I downloaded tha data set file (bupa.data) to a folder (BUPA-Liver_Disorder-data-set) on my desktop.

### Read the data set
I wrote python code to read the data set as shown in Readdata.py file as follows [5]:

f = open('bupa.data', 'r')

s = f.read()

print(s)

f.close()

When the above Readdata.py Python code was run, it generated the full data set in the command prompt interface.

### Calculate the mean value of each column
I calculated the mean value of each column by writing Python code as shown in BUPA.py and the results were as follows follows:

Mean of first column is:  90.15942028985508
Mean of second column is:  69.8695652173913
Mean of third column is:  30.405797101449274
Mean of fourth column is:  24.643478260869564
Mean of fifth column is:  38.28405797101449
Mean of sixth column is:  3.455072463768116
Mean of seventh column is:  1.5797101449275361

import numpy

# Read data file into array.
data = numpy.genfromtxt('bupa.data', delimiter=',')

#python code:
firstcol = data[:,0]
meanfirstcol = numpy.mean(data[:,0])

print("Mean of first column is: ", meanfirstcol)

# Terminal input and output:
In [13]: run mean.py
Mean of first column is:  90.15942028985508

# I calculated the minimum and maxiumum value of each column by writing Python code in the terminal as shown in as follows:

In [9]: numpy.min(firstcol)
Out[9]: 65.0

In [12]: numpy.max(firstcol)
Out[12]: 103.0

# I ran a matplotlib.pyploy command for the furst colum to generate a histogram for the mean corpuscular volume (MCV)column which presented as follows:
Histogram for first column MCV













I calculated the maximum value of each column by writing Python code as shown in maximum.py as follows :




I created plots of the variables by writing Python code as shown in plots.py as follows:




References
1. Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science. Liver Disorders Data Set. 1990. https://archive.ics.uci.edu/ml/datasets/liver+disorders 
2. McDermott, J. & Forsyth, R.S. (2016). Diagnosing a disorder in a classification benchmark. Pattern
Recognition Letters, 73, 41-43. https://www.richardsandesforsyth.net/pubs/JMRF_DiagnosingDisorder_PRL2016.pdf
3. A Little Book of Python for Multivariate Analysis by Yiannis Gatsoulis is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License. Based on a work at A Little Book of R for Multivariate Analysis by Avril Coghlan licensed under CC-BY-3.0. https://python-for-multivariate-analysis.readthedocs.io/
4. Academind. Python for Data Analysis Tutorial - Setup, Read File & First Chart. 2018. https://www.youtube.com/watch?v=cXP_i5-nTXg
5. Ian McLoughlin. Opening files for reading and writing. 2019. https://web.microsoftstream.com/video/72484dfc-1b50-4223-8039-bd6a69cab573
6. Ian McLoughlin. Matplotlib Pyplot video. 2018. https://web.microsoftstream.com/video/f0788c1c-c7bd-4347-98ac-477186938ed7