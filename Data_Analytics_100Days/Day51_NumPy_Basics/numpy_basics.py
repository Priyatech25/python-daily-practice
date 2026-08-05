import numpy as np



arr1 = np.array([10, 20, 30, 40, 50])

print("1D Array:")
print(arr1)

print()

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("2D Array:")
print(arr2)

print()


# Array Properties


print("Shape :", arr2.shape)
print("Dimensions :", arr2.ndim)
print("Size :", arr2.size)
print("Data Type :", arr2.dtype)

print()


# Special Arrays


print("Zeros:")
print(np.zeros((3, 3)))

print()

print("Ones:")
print(np.ones((2, 4)))

print()

print("Identity Matrix:")
print(np.eye(4))

print()

# Range Functions


print("arange:")
print(np.arange(1, 11))

print()

print("linspace:")
print(np.linspace(0, 100, 5))

print()

# Basic Operations


a = np.array([1, 2, 3])

b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Subtraction:", b - a)
print("Multiplication:", a * b)
print("Division:", b / a)

print()


# Statistics


print("Mean:", np.mean(a))
print("Median:", np.median(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print("Sum:", np.sum(a))