import pandas as pd

datHospit = pd.read_csv("../solutions/covid19_hospitalized_switzerland_openzh.csv")

datHospit = datHospit.fillna(0)
print(datHospit.head())

fig = plt.figure(figsize=(20,10))

plt.bar(datHospit['Date'],datHospit['VD'])

plt.xticks(range(len(datHospit['VD'])), datHospit['Date'], rotation=45)
plt.show()


