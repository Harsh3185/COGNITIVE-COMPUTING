import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#1
np.random.seed(102317157)
sales_data = np.random.randint(1000, 5000, (12, 4))
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Sports']
df = pd.DataFrame(sales_data, columns=categories, index=months)
print(df.head())
print(df.describe())

df['Total Sales'] = df.sum(axis=1)
df['Growth Rate'] = df['Total Sales'].pct_change() * 100

total_sales_per_category = df[categories].sum()
total_sales_per_month = df['Total Sales']
avg_growth = df[categories].pct_change().mean()

if 102317157 % 2 == 0:
    df['Electronics'] = df['Electronics'] * 0.9
else:
    df['Clothing'] = df['Clothing'] * 0.85

plt.figure(figsize=(10, 6))
for category in categories:
    plt.plot(df.index, df[category], label=category)
plt.legend()
plt.title('Monthly Sales Trends')
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(data=df[categories])
plt.title('Sales Distribution by Category')
plt.show()

#2
array = np.array([[1, -2, 3], [-4, 5, -6]])
abs_array = np.abs(array)
p25 = np.percentile(array, 25, axis=None)
p50 = np.percentile(array, 50, axis=None)
p75 = np.percentile(array, 75, axis=None)
mean_array = np.mean(array)
median_array = np.median(array)
std_array = np.std(array)

print(abs_array, p25, p50, p75, mean_array, median_array, std_array)

#3
a = np.array([-1.8, -1.6, -0.5, 0.5, 1.6, 1.8, 3.0])
floor_vals = np.floor(a)
ceil_vals = np.ceil(a)
trunc_vals = np.trunc(a)
rounded_vals = np.round(a)

print(floor_vals, ceil_vals, trunc_vals, rounded_vals)

#4
def swap_list_elements(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp
    return lst

lst = [10, 20, 30, 40, 50]
lst = swap_list_elements(lst, 1, 3)
print(lst)

#5
s = {1, 2, 3, 4}
s_list = list(s)
s_list[0], s_list[1] = s_list[1], s_list[0]
s = set(s_list)
print(s)
