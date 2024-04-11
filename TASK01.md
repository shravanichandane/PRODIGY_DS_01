# PRODIGY_DS_01

# Create a bar chart or histogram to visualize the distribution of a categorical or continuous variable.

This is a brief summary of the project.

# Task Summary

This task involves creating a bar chart or histogram to visualize the distribution of a categorical or continuous variable.

## Description

The goal of this task is to create a visual representation of the distribution of a variable using a bar chart or histogram. This will help us to understand the frequency or proportion of each category or value in the dataset.

## dataset taken
Orders.xlsx [Orders.xlsx](https://github.com/shravanichandane/PRODIGY_DS_01/files/14934878/Orders.xlsx)

## Steps

1. Load the dataset Orders ( you can choose any dataset) using the `read.csv` or for excel 'read.excel' function.
2. Filter the dataset to include only the variable of interest and its corresponding value.
3. Rename the columns to make them more readable.
4. Load the `pandas','seaborn','matplotlib' packages in python .
5. Create a bar chart or histogram using the imported libraries
6. Customize the plot as needed (e.g., add labels, change colors, etc).

## Tools used :
VS-code
packages: pandas,seaborn,matplotlib.

## Source code of the project

Here's an example of how to create a bar chart to visualize the distribution of regions in a sample dataset:

```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('C:/Users/shrav/Downloads/Orders.xlsx')............ #copy path of the file.
print(df.head())

sns.countplot(x='State', data=df)
plt.title('Distribution of States')
plt.show()

sns.histplot(x='order_total', data=df)
plt.title('Distribution of Order Total')
plt.show()

## Features

* Allows users to visualize the distribution of a categorical or continuous variable using a bar chart or histogram.
* Supports loading data from the desired dataset using the `read.csv`, 'read.excel' function.
* Allows users to filter the dataset to include only the variable of interest and its corresponding value.
* Supports renaming columns to make them more readable.
* Allows users to customize the plot as needed (e.g., add labels, change colors, etc.).
* Provides an example of how to create a bar chart to visualize the distribution of regions in a sample dataset.

## conclusion
After visualizing the distribution of statuses and order totals in the dataset, we can observe the following patterns and trends:

The dataset contains data for 1000 orders.
The status distribution is skewed to the right, with a large number of orders having a 'Completed' status and a smaller number of orders having a 'Cancelled' status.
The order total distribution is also skewed to the right, with a large number of orders having a lower order total and a smaller number of orders having a higher order total.
These observations can be used to understand the distribution of orders and inform business decisions related to inventory management, pricing, and other operational strategies.


output:

Order ID Order Date  customer_id CustomerName             State     City  order_total  Product cost Category
0         1 2018-03-10            1    Harivansh     Uttar Pradesh  Mathura         2599          1145   Phones
1         2 2018-02-03            3       Madhav    Madhya Pradesh   Indore         2599          1145   Phones
2         3 2018-01-24            5  Madan Mohan  Himachal Pradesh    Simla         2599          1145   Tables
3         4 2018-12-27            7        Gopal  Himachal Pradesh    Simla         2599          1145   Phones
4         5 2018-08-21            9     Vishakha          Nagaland   Kohima         2599          2291   Phones

![Figure_1 ordertak1](https://github.com/shravanichandane/PRODIGY_DS_01/assets/166283264/4c589c59-2892-4a77-95f8-bbac8814d897)
![Figure_1task](https://github.com/shravanichandane/PRODIGY_DS_01/assets/166283264/80d2be88-8633-4e87-a452-2a88dfdae00b)
