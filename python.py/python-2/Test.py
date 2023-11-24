import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("/Users/pagadalas11gmail.com/Documents/Book2.xlsx")
data = data.set_index("Date")
print(data)

data['Load Shedding'] = data['Load Shedding'].map({"Yes": 1,"No": 0})

print(data)
fig, ax = plt.subplots(4,1)


ax[0].plot(data.index, data['PV kWh'])
ax[0].set_title("PV consumption")
ax[0].set_xlabel("Date")
ax[0].set_ylabel("Time (Min)")
ax[1].plot(data.index, data['Load Variation'])
ax[1].set_title("Load consumption")
ax[1].set_xlabel("Date")
ax[1].set_ylabel("Time (Min)")
ax[2].plot(data.index, data['SOC of the battery'])
ax[2].set_title("Battery Utilization")
ax[2].set_xlabel("Date")
ax[2].set_ylabel("Time (Min)")
ax[3].bar(data.index, data['Load Shedding'])
ax[3].set_title("Load shedding period")
ax[3].set_xlabel("Date")
ax[3].set_ylabel("Yes / No")
plt.tight_layout()

# to find the corelation 
data = pd.read_excel("/Users/pagadalas11gmail.com/Documents/Book2.xlsx")
data['Load Shedding'] = data['Load Shedding'].map({"Yes": 1,"No": 0})

print(data. corr())

sns.heatmap(data.corr(), annot=True)

data=data.reset_index()
data['Weekday'] = data['Date'].dt.weekday

data['Is_Sunday'] = data['Weekday'] == 6
print(data)

sns.lineplot(data=data, x="Date", y="SOC of the battery")
sns.scatterplot(data=data, x="Date", y="SOC of the battery", hue="Is_Sunday")
plt.show()