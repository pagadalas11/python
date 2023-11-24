import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("/Users/pagadalas11gmail.com/Documents/Book2.xlsx")

data['Load Shedding'] = data['Load Shedding'].map({"Yes": 1,"No": 0})


data=data.reset_index()
data['Weekday'] = data['Date'].dt.weekday

data['Is_Sunday'] = data['Weekday'] == 6
print(data)

sns.lineplot(data=data, x="Date", y="PV kWh")
sns.scatterplot(data=data, x="Date", y="Load kWh", hue="Is_Sunday")
plt.show()

