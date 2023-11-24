import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("______")
data = data.set_index("Date")
print(data)

plt.plot(data.index, data['PV kWh'])
plt.show()
