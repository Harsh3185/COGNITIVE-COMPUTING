#1
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

M = float(input("Enter a value for M: "))

x = np.linspace(-10, 10, 400)

y1 = M * x**2
y2 = M * np.sin(x)

plt.figure(figsize=(8,6))
plt.plot(x, y1, 'r-', label=f'y = {M}x^2')
plt.plot(x, y2, 'b--', label=f'y = {M}sin(x)')
plt.legend()
plt.grid(True)
plt.title("Mathematical Function Plots")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


#2

data = {
    'Subjects': ['Math', 'Science', 'English', 'History', 'Art'],
    'Scores': [85, 90, 78, 88, 76]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8,6))
ax = sns.barplot(x='Subjects', y='Scores', data=df, palette='muted')

for p in ax.patches:
    ax.annotate(f"{p.get_height()}", (p.get_x() + p.get_width()/2, p.get_height()),
                 ha='center', va='bottom', fontsize=12)

plt.title("Scores of 5 Subjects")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.grid(axis='y')
plt.show()


#3

roll_number = 102317157
np.random.seed(roll_number)

data = np.random.randn(50)

cumsum = np.cumsum(data)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].plot(cumsum, 'g-', label="Cumulative Sum")

axes[0].set_title("Cumulative Sum Plot")
axes[0].legend()
axes[0].grid()

axes[1].scatter(range(50), data, c='red', label="Random Noise")
axes[1].set_title("Scatter Plot")

axes[1].legend()
axes[1].grid()

plt.tight_layout()
plt.show()


#4

url = "https://raw.githubusercontent.com/AnjulaMehto/MCA/main/company_sales_data.csv"
df = pd.read_csv(url)

plt.figure(figsize=(8,6))
sns.lineplot(x=df['month_number'], y=df['total_profit'], marker='o', color='g')
plt.title("Total Profit Over Months")
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.grid(True)
plt.show()

plt.figure(figsize=(8,6))
for column in df.columns[1:-1]:
    sns.lineplot(x=df['month_number'], y=df[column], label=column)
plt.title("Product Sales Over Months")
plt.xlabel("Month Number")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()

df.plot(kind='bar', figsize=(12,6), alpha=0.75)
plt.title("Company Sales Data")
plt.xlabel("Month Number")
plt.ylabel("Values")
plt.legend(loc='upper right')
plt.show()
