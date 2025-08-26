threshold = 0.01
pvalue_counter = 0

for pv in pvalue_list:
    if pv < threshold:
        pvalue_counter += 1

print("Number of p-values under ", threshold, ": ", pvalue_counter, sep="")
