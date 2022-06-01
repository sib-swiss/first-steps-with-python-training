
import numpy as np
import scipy.stats as stats

# 1. Load the data from the input "sample_data.tsv" file
# ******************************************************

# Note that we skip the first row because it contains the column names, and 
# we here load the data as a matrix, not as a DataFrame.
input_file = "data/sample_data.tsv"
data = np.loadtxt(input_file, dtype=float, delimiter='\t', skiprows=1)

# Load the header of the file separately.
with open(input_file, mode="r") as f:
    line = f.readline() # Read the first line of the file - contains header.
    header = line.strip().split('\t') # Split it to get the column names.

# Display the matrix dimension and column names.
print("The dimension of the data matrix is:", data.shape)
print("The column names of the matrix are :", header)

# Showing the first 3 lines of the matrix. 
print(data[0:3,])


# 2. Log-transform the data
# *************************
# Log-transform the data in base 2 log.
log_data = np.log2(data)
print(log_data[0:3,])


# 3. Compute row-wise means for replicates of Sample1 and Sample2
# ***************************************************************
# The values for sample 1 and sample 2 are distributed over several columns,
# so we first need to identify the indices of columns for sample 1, and 2.
# We use the column names to identify the sample to which they belong.
s1_columns = []
s2_columns = []
for i , column_name in enumerate(header):
    if column_name.startswith('Sample1'):
        s1_columns.append(i)
    elif column_name.startswith('Sample2'):
        s2_columns.append(i)

# Now that we have the indices of columns, it is fairly easy to compute
# row-wise means for the columns of each sample.
mean_s1 = np.mean(log_data[:, s1_columns], axis=1)
mean_s2 = np.mean(log_data[:, s2_columns], axis=1)
print("Mean values per row for sample 1 replicates:\n", mean_s1)
print("Mean values per row for sample 2 replicates:\n", mean_s2)


# 4. Compute row-wise standard deviations
# ***************************************
std_s1 = np.std(log_data[:, s1_columns], axis=1)
std_s2 = np.std(log_data[:, s2_columns], axis=1)
print("Std values per row for sample 1 replicates:\n", mean_s1)
print("Std values per row for sample 2 replicates:\n", mean_s2


# 5. Use a function *scipy.stats.ttest_ind* to calculate p-value for every row

TTest_pValues = stats.ttest_ind(log_data[:,s1_columns], log_data[:,s2_columns], axis=1, equal_var=False).pvalue

# 6. Select p-values which are smaller than $10^{-2}$

significant = TTest_pValues < 10**-2

# 7. Print how many P-values below $10^{-2}$ are found

print( 'there are',sum(significant),'p-values <0.01.')