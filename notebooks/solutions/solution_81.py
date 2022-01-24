# 1. Load the data in thefile "sample_data.tsv" as a numpy array

import numpy as np
import scipy.stats as stats

#the loading itself is not hard
data = np.loadtxt("data/sample_data.tsv", dtype=np.float,delimiter='\t', skiprows=1) #notice I skip the first row

#I load the header separately
IN = open("data/sample_data.tsv",'r')
l = IN.readline() #read the first line
header = l.strip().split('\t') #split it to get the header
IN.close()#no need to go further than that

print( data.shape )
print(header)
#showing the first 5 lines 
print(data[0:5,])

# 2. Log-transform the data

log_data = np.log2(data)

print(log_data[0:5,])


# 3. Find the row-wise means for replicates of Sample1 and Sample2

print(header)
#first, I will create lists containing the indexes of columns for both samples
sample1_columns = []
sample2_columns = []
for i , column_name in enumerate(header):
    if column_name.startswith('Sample1'):
        sample1_columns.append(i)
    elif column_name.startswith('Sample2'):
        sample2_columns.append(i)

print('sample 1')
print(log_data[0:2,sample1_columns])
print('sample 2')
print(log_data[0:2,sample2_columns])


#now, it is fairly easy to get the row-wise means
meanSample1 = np.mean(log_data[:,sample1_columns], axis=1)
meanSample2 = np.mean(log_data[:,sample2_columns], axis=1)


# 4. Find the row-wise standard deviations the same way as means

stdSample1 = np.std(log_data[:,sample1_columns], axis=1)
stdSample2 = np.std(log_data[:,sample2_columns], axis=1)

# 5. Use a function *scipy.stats.ttest_ind* to calculate p-value for every row

TTest_pValues = stats.ttest_ind(log_data[:,sample1_columns], log_data[:,sample2_columns], axis=1, equal_var=False).pvalue

# 6. Select p-values which are smaller than $10^{-2}$

significant = TTest_pValues < 10**-2

# 7. Print how many P-values below $10^{-2}$ are found

print( 'there are',sum(significant),'p-values <0.01.')