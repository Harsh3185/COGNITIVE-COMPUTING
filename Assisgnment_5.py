import numpy as np
import matplotlib.pyplot as plt

#1
gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')
print(np.sum(gfg))
print(np.sum(gfg, axis=1))
print(np.sum(gfg, axis=0))


#2
array = np.array([10, 52, 62, 16, 16, 54, 453])
print(np.sort(array))
print(np.argsort(array))
print(np.sort(array)[:4])
print(np.sort(array)[-5:])



array = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])
print(array[array == array.astype(int)])
print(array[array != array.astype(int)])



#3
initials_ascii_sum = sum(ord(char) for char in "AB")
sales = np.array([initials_ascii_sum + i * 50 for i in range(5)])
tax_rate = ((initials_ascii_sum % 5) + 5) / 100
print(sales * (1 + tax_rate))
discounted_sales = np.where(sales < initials_ascii_sum + 100, sales * 0.95, sales * 0.90)
print(discounted_sales)

sales_matrix = np.vstack([sales] * 3)
weekly_growth = np.array([1.00, 1.02, 1.04]).reshape(3, 1)
adjusted_sales_matrix = sales_matrix * weekly_growth
print(adjusted_sales_matrix)



#4
x = np.linspace(-10, 10, 100)
plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.plot(x, x**2)
plt.title("Y = x^2")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(x, np.sin(x))
plt.title("Y = sin(x)")
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(x, np.exp(x))
plt.title("Y = e^x")
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(x, np.log(np.abs(x) + 1))
plt.title("Y = log(|x| + 1)")
plt.grid(True)

plt.tight_layout()
plt.show()