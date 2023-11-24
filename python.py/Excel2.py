import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np

data = pd.read_excel("/Users/pagadalas11gmail.com/Documents/Book1.xlsx")

data['Load Shedding'] = data['Load Shedding'].map({"Yes": 1,"No": 0})


fig, sns= plt.subplots(5,1)

sns[0].plot(data.index, data['PV kWh'])
sns[0].set_title("Pv data")
sns[0].set_xlabel("Date")
sns[0].set_ylabel("Time (Min)")
sns[1].plot(data.index, data['Load kWh'])
sns[1].set_title("Load Consumption")
sns[1].set_xlabel("Date")
sns[1].set_ylabel("Time (Min)")
sns[2].plot(data.index, data['SOC of the battery'])
sns[2].set_title("battery consumption")
sns[2].set_xlabel("Date")
sns[2].set_ylabel("Time (Min)")
sns[3].plot(data.index, data['Grid to Bat'])
sns[3].set_title("Grid Consumpttoin")
sns[3].set_xlabel("Date")
sns[3].set_ylabel("Time (Min)")
sns[4].bar(data.index, data['Load Shedding'])
sns[4].set_title("Load shedding period")
sns[4].set_xlabel("Date")
sns[4].set_ylabel("Yes / No")
plt.tight_layout()
plt.show()

# to find the corelation 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data = pd.read_excel("/Users/pagadalas11gmail.com/Documents/Book1.xlsx")

data['Load Shedding'] = data['Load Shedding'].map({"Yes": 1,"No": 0})

print(data. corr())

sns.heatmap(data.corr(), annot=True)
plt.show()


data["SOC of the battery"] = data["SOC of the battery"]
data=data.reset_index()
data["Weekday"] = data["Date"].dt.weekday

data["Is_Sunday"] = data["Weekday"] == 6
print(data)
sns.lineplot(data=data, x="Date", y="SOC of battery")
sns.scatterplot(data=data,x="Date", y="SOC of battery", hue="Is_Sunday")
plt.show()