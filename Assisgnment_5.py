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
X = ord('H')+ord('C')
sales = np.array([X, X + 50, X + 100, X + 150, X + 200])
print("Sales array:", sales)

tax_rate = ((X % 5) + 5) / 100
print(tax_rate)
sales_after_tax = sales * (1 - tax_rate)
print("Sales after tax:", sales_after_tax)

discounted_sales = np.where(sales < X+100, sales_after_tax * 0.95, sales_after_tax * 0.90)
print("Discounted sales:", discounted_sales)

sales_weeks = np.array([sales, sales * 1.02, sales * 1.02**2])
print("Sales over 3 weeks:\n", sales_weeks)



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