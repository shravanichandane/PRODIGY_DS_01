import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('C:/Users/shrav/Downloads/Orders.xlsx')
print(df.head())

sns.countplot(x='State', data=df)
plt.title('Distribution of States')
plt.show()

sns.histplot(x='order_total', data=df)
plt.title('Distribution of Order Total')
plt.show()