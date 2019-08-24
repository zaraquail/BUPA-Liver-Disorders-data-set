# BUPA-Liver-Disorders-data-set August 2019 Programming and Scripting Project

## Higher Diploma in Data Analytics Course, Galway Mayo Institute of Technology

## Zara Quail

### BUPA Liver Disorders Data Set Summary
Note: reference citations are denoted as bold numbers in square brackets

The BUPA Liver Disorders data set was created by BUPA Medical Research Limited and was donated to the UCI Machine Learning Repository by Richard S. Forsyth in May 1990.**[1]** The data set is multivariate and includes categorical, integer and real attributes.**[1]** Each line of the data records  7 variables from one of a total of 345 male individuals.**[1]** The variables represented include the results of 5 blood tests that are considered potentially indicative of liver disorders that are caused by drinking excess alcohol.**[1]** The blood test results are the first 5 variables and include: 1) mean corpuscular volume (MCV), 2) alkaline phosphatase (alk phos), 3) alanine aminotransferase (sgpt), 4) aspartate aminotransferase (sgot), 5) gamma-glutamyl transpeptidase (gamma gt). The sixth variable is the number of half-pint equivalents of alcoholic beverages drunk per day (drinks) and the seventh variable is the selector field created by the BUPA researchers to split the data into train/test sets.**[1]** The data set would be considered to be complete as there are no missing values.**[1]** It is noted that the data set does not present any variables that denote the presence or absence of a liver disorder for each of the individuals.**[1]** The data set has often been utilised as a benchmark dataset.**[2]** However,  as noted by authors McDermott and Forsyth in 2016, the last variable of the data set has been incorrectly interpreted by some as a classification label, rather than the test/train indicator, resulting in useless results and potentially dangerous and incorrect assignment of a liver disease to an individual.**[2]** In addition, duplicates have been noted in the following data set rows **[1]**:

row 84 and 86:   94,58,21,18,26,2.0,2

row 141 and 318:   92,80,10,26,20,6.0,1

row 143 and 150:   91,63,25,26,15,6.0,1

row 170 and 176:   97,71,29,22,52,8.0,1

### Downloading the Data set

I downloaded tha data set file (bupa.data) to a folder (BUPA-Liver_Disorder-data-set) on my desktop.

### Read the data set
I wrote python code to read the data set as shown in Readdata.py file as follows **[5]**:

f = open('bupa.data', 'r')

s = f.read()

print(s)

f.close()

When the above Readdata.py Python code was run, it generated the full data set in the command prompt interface.

### Calculating the mean value of each column
I calculated the mean value of each column by writing Python code as shown in BUPAMean.py and the results were as follows and also displayed in *Table 1* **[6]**:

Mean of first column is:  90.15942028985508

Mean of second column is:  69.8695652173913

Mean of third column is:  30.405797101449274

Mean of fourth column is:  24.643478260869564

Mean of fifth column is:  38.28405797101449

Mean of sixth column is:  3.455072463768116

Mean of seventh column is:  1.5797101449275361

**Table 1: Mean Values for Columns in BUPA Liver Disorders Data set**

MCV | alkphos | sgpt | sgot | gammagt | drinks | train/test sets
--- | ------- | ---- | ---- | ------- | ------ | ---------------
90.15942028985508 | 69.8695652173913 | 30.405797101449274 | 24.643478260869564 | 38.28405797101449 | 3.455072463768116 | 1.5797101449275361

As an example for the first column the code was as shown below and for each subsequent column I increase the number after the , in the bracket [:,1][:,2] etc as shown in BUPAMean.py file.**[6]**

import numpy

>Read data file into array.
data = numpy.genfromtxt('bupa.data', delimiter=',')

>python code
firstcol = data[:,0]
meanfirstcol = numpy.mean(data[:,0])

print("Mean of first column is: ", meanfirstcol)

**Histograms for each column**

I ran a matplotlib.pyploy command within the Python code in BUPAMean.py file for each column to generate a histogram for each column.**[6]** I saved the generated histogram fo each column and later edited them in 3D Paint to add titles and lable the x and y axes. I noticed that including the Python code for the matplotlib.pyploy commands after the code for the mean values in the same python file, I had to save and close each histogram as it was generated before the code would continue to run for the remaining columns.

**Histograms for Columns in BUPA Liver Disorders Data set**
![Column1_MCV_Histogram](https://github.com/zaraquail/BUPA-Liver-Disorders-data-set/blob/master/Column1_MCV_Histogram.png)

![Column2_alkphos_Histogram](https://github.com/zaraquail/BUPA-Liver-Disorders-data-set/blob/master/Column2_alkphos_Histogram.png)

![Column3_sgpt_Histogram](https://github.com/zaraquail/BUPA-Liver-Disorders-data-set/blob/master/Column3_sgpt_Histogram.png)

![Column4_sgot_Histogram](https://github.com/zaraquail/BUPA-Liver-Disorders-data-set/blob/master/Column4_sgot_Histogram.png)

![Column5_gammagt_Histogram](https://github.com/zaraquail/BUPA-Liver-Disorders-data-set/blob/master/Column5_gammagt_Histogram.png)

![Column6_drinks_Histogram](https://github.com/zaraquail/BUPA-Liver-Disorders-data-set/blob/master/Column6_drinks_Histogram.png)

![Column7_traintestsets_Histogram](https://github.com/zaraquail/BUPA-Liver-Disorders-data-set/blob/master/Column7_traintestsets_Histogram.png)


### Calculating the minimum value of each column
The minimum values of each columns are presented in *table 2* below.

**Table 2: Minimum Values for Columns in BUPA Liver Disorders Data set**

MCV | alkphos | sgpt | sgot | gammagt | drinks | train/test sets
--- | ------- | ---- | ---- | ------- | ------ | ---------------
65.0 | 23.0 | 4.0 | 5.0 | 5.0 | 0.0 | 1.0


I calculated the minimum and maxiumum value of each column by writing Python code in the terminal as shown in as follows **[7]**:

In [9]: numpy.min(firstcol)
Out[9]: 65.0

In [5]: numpy.min(secondcol)
Out[5]: 23.0

In [6]: numpy.min(thirdcol)
Out[6]: 4.0

In [7]: numpy.min(fourthcol)
Out[7]: 5.0

In [8]: numpy.min(fifthcol)
Out[8]: 5.0

In [9]: numpy.min(sixthcol)
Out[9]: 0.0

In [10]: numpy.min(seventhcol)
Out[10]: 1.0

### Calculating the maximum value of each column
The maximum values of each columns are presented in *table 3* below.

**Table 3: Maximum Values for Columns in BUPA Liver Disorders Data set**

MCV | alkphos | sgpt | sgot | gammagt | drinks | train/test sets
--- | ------- | ---- | ---- | ------- | ------ | ---------------
103.0 | 138.0 | 155.0 | 82.0 | 297.0 | 20.0 | 2.0

I calculated the minimum and maxiumum value of each column by writing Python code in the terminal as shown in as follows **[7]**:

In [12]: numpy.max(firstcol)
Out[12]: 103.0

In [11]: numpy.max(secondcol)
Out[11]: 138.0

In [12]: numpy.max(thirdcol)
Out[12]: 155.0

In [13]: numpy.max(fourthcol)
Out[13]: 82.0

In [14]: numpy.max(fifthcol)
Out[14]: 297.0

In [15]: numpy.max(sixthcol)
Out[15]: 20.0

In [16]: numpy.max(seventhcol)
Out[16]: 2.0

### Conclusion
The BUPA Liver Disorders data set is a good example of a multivariate data set. In this project I have demonstrated how Python can be used to assess a data set by using Python code to calculate the mean, maximum and minimum values and generate histograms for each column. The project has also made use of Git and Git Hub for commits and pushes of the files to my Git Hub repository. It is thanks to the lecturer that I was able to complete this.

### References
1. Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science. Liver Disorders Data Set. 1990. https://archive.ics.uci.edu/ml/datasets/liver+disorders 
2. McDermott, J. & Forsyth, R.S. (2016). Diagnosing a disorder in a classification benchmark. Pattern
Recognition Letters, 73, 41-43. https://www.richardsandesforsyth.net/pubs/JMRF_DiagnosingDisorder_PRL2016.pdf
3. A Little Book of Python for Multivariate Analysis by Yiannis Gatsoulis is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License. Based on a work at A Little Book of R for Multivariate Analysis by Avril Coghlan licensed under CC-BY-3.0. https://python-for-multivariate-analysis.readthedocs.io/
4. Academind. Python for Data Analysis Tutorial - Setup, Read File & First Chart. 2018. https://www.youtube.com/watch?v=cXP_i5-nTXg
5. Ian McLoughlin. Opening files for reading and writing. 2019. https://web.microsoftstream.com/video/72484dfc-1b50-4223-8039-bd6a69cab573
6. Ian McLoughlin. Matplotlib Pyplot video. 2018. https://web.microsoftstream.com/video/f0788c1c-c7bd-4347-98ac-477186938ed7
7. Ian McLoughlin. Numpy video. 2018  https://web.microsoftstream.com/video/74b18405-5ee1-47f0-a42d-e8831a453a91