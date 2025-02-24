import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#1
np.random.seed(102317157)
data_matrix = np.random.randint(1000, 5001, size=(12, 4))
labels = ['Electronics', 'Clothing', 'Home & Kitchen', 'Sports']
time_periods = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
data_frame = pd.DataFrame(data_matrix, columns=labels, index=time_periods)
print(data_frame.head())
print(data_frame.describe())

data_frame['Total Sales'] = data_frame.sum(axis=1)
data_frame['Growth Rate'] = data_frame['Total Sales'].pct_change() * 100

total_per_category = data_frame[labels].sum()
total_per_month = data_frame['Total Sales']
average_growth = data_frame[labels].pct_change().mean()

if 102317157 % 2 == 0:
    data_frame['Electronics'] *= 0.9
else:
    data_frame['Clothing'] *= 0.85

plt.figure(figsize=(10, 6))
sns.lineplot(data=data_frame[labels])
plt.title("Monthly Sales Trends")
plt.xlabel("Month")
plt.ylabel("Sales Units")
plt.legend(labels)
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(data=data_frame[labels])
plt.title("Sales Distribution by Category")
plt.show()

#2
data_array = np.array([[1, -2, 3], [-4, 5, -6]])
absolute_values = np.abs(data_array)
quartiles_flat = np.percentile(data_array.flatten(), [25, 50, 75])
quartiles_columns = np.percentile(data_array, [25, 50, 75], axis=0)
quartiles_rows = np.percentile(data_array, [25, 50, 75], axis=1)

mean_flat = np.mean(data_array)
mean_cols = np.mean(data_array, axis=0)
mean_rows = np.mean(data_array, axis=1)

median_flat = np.median(data_array)
median_cols = np.median(data_array, axis=0)
median_rows = np.median(data_array, axis=1)

std_flat = np.std(data_array)
std_cols = np.std(data_array, axis=0)
std_rows = np.std(data_array, axis=1)

print(absolute_values, quartiles_flat, quartiles_columns, quartiles_rows, mean_flat, mean_cols, mean_rows, median_flat, median_cols, median_rows, std_flat, std_cols, std_rows)

#3
values = np.array([-1.8, -1.6, -0.5, 0.5, 1.6, 1.8, 3.0])
floor_values = np.floor(values)
ceil_values = np.ceil(values)
truncate_values = np.trunc(values)
round_values = np.round(values)

print(floor_values, ceil_values, truncate_values, round_values)

#4
def switch_elements(lst, idx1, idx2):
    buffer = lst[idx1]
    lst[idx1] = lst[idx2]
    lst[idx2] = buffer
    return lst

list_sample = [10, 20, 30, 40, 50]
list_sample = switch_elements(list_sample, 1, 3)
print(list_sample)

#5
set_sample = {10, 20, 30, 40, 50}
set_list = list(set_sample)
set_list[1], set_list[3] = set_list[3], set_list[1]
set_sample = set(set_list)
print(set_sample)