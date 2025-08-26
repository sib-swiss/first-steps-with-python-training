import pandas as pd
import matplotlib.pyplot as plt

data_hospit = pd.read_csv("../solutions/covid19_hospitalized_switzerland_openzh.csv")

data_hospit = data_hospit.fillna(0)
print(data_hospit.head())

fig = plt.figure(figsize=(20,10))

plt.bar(data_hospit['Date'],data_hospit['VD'])

plt.xticks(range(len(data_hospit['VD'])), data_hospit['Date'], rotation=45)
plt.show()


