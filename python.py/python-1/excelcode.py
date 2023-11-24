import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("/Users/pagadalas11gmail.com/Documents/Book1.xlsx")
data = data.set_index("Date")
print(data)

plt.plot(data.index, data['SOC of the battery '])
plt.show()
