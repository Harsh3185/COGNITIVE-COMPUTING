# 1
import numpy as np

arr = np.array([5, 10, 15, 20, 25])
print("Original Array:", arr)

# 1-a
print("After Addition:", arr + 2)

# 1-b
print("After Multiplication:", arr * 3)

# 1-c
print("After Division:", arr / 2)

# 2
arr = np.array([1, 2, 3, 6, 4, 5])
print("Original Array:", arr)

# 2-a
arr_rev = arr[::-1]
print("Reversed Array:", arr_rev)

# 2-b
x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])

most_freq_x = np.bincount(x).argmax()
indices_x = np.where(x == most_freq_x)[0]

most_freq_y = np.bincount(y).argmax()
indices_y = np.where(y == most_freq_y)[0]

print("Most Frequent in x:", most_freq_x, "at indices", indices_x)
print("Most Frequent in y:", most_freq_y, "at indices", indices_y)

# 3
arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# 3-a
print("1st row, 2nd column:", arr[0, 1])

# 3-b
print("3rd row, 1st column:", arr[2, 0])

# 4
harsh = np.linspace(10, 100, 25)
print("Array:", harsh)

print("Dimensions:", harsh.ndim)
print("Shape:", harsh.shape)
print("Total Elements:", harsh.size)
print("Data Type:", harsh.dtype)
print("Total Bytes:", harsh.nbytes)

reshaped = harsh.reshape(25, 1)
print("Transpose using reshape:\n", reshaped)
print("Transpose using T attribute:\n", reshaped.T)

# 5
ucs420_harsh = np.array([[10, 20, 30, 40], [50, 60, 70, 80], [90, 15, 20, 35]])

print("Mean:", np.mean(ucs420_harsh))
print("Median:", np.median(ucs420_harsh))
print("Max:", np.max(ucs420_harsh))
print("Min:", np.min(ucs420_harsh))
print("Unique Elements:", np.unique(ucs420_harsh))

reshaped_ucs420 = ucs420_harsh.reshape(4, 3)
resized_ucs420 = ucs420_harsh[:2, :3]

print("Original:\n", ucs420_harsh)
print("Reshaped (4x3):\n", reshaped_ucs420)
print("Resized (2x3):\n", resized_ucs420)
