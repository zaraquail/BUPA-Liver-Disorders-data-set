# BUPA-Liver-Disorders-data-set
August 2019 Programming and Scripting Project

Higher Diploma in Data Analytics Course, Galway Mayo Institute of Technology

Zara Quail 

BUPA Liver Disorders Data Set Summary

The BUPA Liver Disorders data set was created by BUPA Medical Research Limited and was donated to the UCI Machine Learning Repository by Richard S. Forsyth in May 1990.[1] The data set is multivariate and includes categorical, integer and real attributes.[1] Each line of the data records  7 variables from one of a total of 345 male individuals.[1] The variables represented include the results of 5 blood tests that are considered potentially indicative of liver disorders that are caused by drinking excess alcohol.[1] The blood test results are the first 5 variables and include: 1) mean corpuscular volume (MCV), 2) alkaline phosphatase (alk phos), 3) alanine aminotransferase (sgpt), 4) aspartate aminotransferase (sgot), 5) gamma-glutamyl transpeptidase (gamma gt). The sixth variable is the number of half-pint equivalents of alcoholic beverages drunk per day (drinks) and the seventh variable is the selector field created by the BUPA researchers to split the data into train/test sets.[1] The data set would be considered to be complete as there are no missing values. [1] It is noted that the data set does not present any variables that denote the presence or absence of a liver disorder for each of the individuals.[1] The data set has often been utilised as a benchmark dataset.[2] However,  as noted by authors McDermott and Forsyth in 2016, the last variable of the data set has been incorrectly interpreted by some as a classification label, rather than the test/train indicator, resulting in useless results and potentially dangerous and incorrect assignment of a liver disease to an individual.[2] In addition, duplicates have been noted in the following data set rows:[1]

row 84 and 86:   94,58,21,18,26,2.0,2

row 141 and 318:   92,80,10,26,20,6.0,1

row 143 and 150:   91,63,25,26,15,6.0,1

row 170 and 176:   97,71,29,22,52,8.0,1

References
1. Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science. Liver Disorders Data Set. 1990. https://archive.ics.uci.edu/ml/datasets/liver+disorders 
2. McDermott, J. & Forsyth, R.S. (2016). Diagnosing a disorder in a classification benchmark. Pattern
Recognition Letters, 73, 41-43. https://www.richardsandesforsyth.net/pubs/JMRF_DiagnosingDisorder_PRL2016.pdf
