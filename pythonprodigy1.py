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


output:
 Order ID Order Date  customer_id CustomerName             State     City  order_total  Product cost Category
0         1 2018-03-10            1    Harivansh     Uttar Pradesh  Mathura         2599          1145   Phones
1         2 2018-02-03            3       Madhav    Madhya Pradesh   Indore         2599          1145   Phones
2         3 2018-01-24            5  Madan Mohan  Himachal Pradesh    Simla         2599          1145   Tables
3         4 2018-12-27            7        Gopal  Himachal Pradesh    Simla         2599          1145   Phones
4         5 2018-08-21            9     Vishakha          Nagaland   Kohima         2599          2291   Phones

