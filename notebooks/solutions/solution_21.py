threshold = 0.01
pvNumber = 0
for pv in pvalue_list:
    if pv < threshold:
        pvNumber += 1
print("number of pv-values under",threshold,":",pvNumber)
