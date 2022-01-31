import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
#1. How many negative numbers are there?
len(a[a < 0])
# There are four negative numbers.

#2. How many positive numbers are there?
len(a[a > 0])
# There are five positive numbers

#3. How many even positive numbers are there?
b= a[a % 2 == 0]
len(b[b > 0])
# Can use & (and) | (or) as well inside of the [] for comparisons
# There are three elements that satisfy those conditions.

#4. If you were to add 3 to each data point, how many positive numbers would there be?
b = a + 3
len(b[b > 0])
# There are ten elements that satisfy those conditions.

#5. If you squared each number, what would the new mean and standard deviation be?
m = a.mean()
st = a.std()
print(m)
print(st)
# Current mean = 3, current std = 8.06
new_a = a ** 2
new_m = new_a.mean()
new_st = new_a.std()
print(new_m)
print(new_st)
# New mean = 74, new std = 144.02

#6. Center the data (subtract the mean)
a_center = a - m
print(a_center)

#7. Calculate z-score for each data point
z_scores = (a - m) / st
print(z_scores)

# Life w/o numpy to life with numpy
## Setup 1

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = (sum(a) / len(a))
# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
def multiply_all(l):
    result = 1
    for n in l:
        result = result * n
    return result
product_of_a = multiply_all(a)
print(product_of_a) 
# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
def squared(li):
    squares = []
    for n in li:
        n = n ** 2
        squares.append(n)
    return squares
squares_of_a = squared(a)
print(squares_of_a)
# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = [n for n in a if n % 2 != 0]
print(odds_in_a)
# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = [n for n in a if n % 2 == 0]
## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
import numpy as np
b = [
    [3, 4, 5],
    [6, 7, 8]
]
# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
print(sum_of_b)
b = np.array(b)
sum_of_b = b.sum()
print(sum_of_b)
# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])
print(min_of_b)  
min_of_b = b.min()
# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
max_of_b = b.max()
# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
print(mean_of_b)
mean_of_b = b.mean()
# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
product_of_b = b.prod()
# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
squares_of_b = b ** 2
print(squares_of_b)
# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
odds_in_b = b[b % 2 != 0]
print(odds_in_b)
# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
evens_in_b = b[b % 2 == 0]
# Exercise 9 - print out the shape of the array b.
print(b.shape)
# Exercise 10 - transpose the array b.
transposed_b = b.transpose()
print(transposed_b)
# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
shape_1_6 = b.reshape(1, 6)
print(shape_1_6)
# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
shape_6_1 = b.reshape(6,1)
print(shape_6_1)

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
c = np.array(c)
min_c = c.min()
max_c = c.max()
sum_c = c.sum()
prod_c = c.prod()
# Exercise 2 - Determine the standard deviation of c.
stdv_c = c.std()
# Exercise 3 - Determine the variance of c.
var_c = np.var(c)
# Exercise 4 - Print out the shape of the array c
print(c.shape)
# Exercise 5 - Transpose c and print out transposed result.
transposed_c = c.transpose()
print(transposed_c)
# Exercise 6 - Get the dot product of the array c with c. 
dotted = np.dot(c, c)
# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
product_c_ct = c * transposed_c
sum_product_c_ct = product_c_ct.sum()
print(sum_product_c_ct)
# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
prod_product_c_ct = product_c_ct.prod()
print(prod_product_c_ct)

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d = np.array(d)
# Exercise 1 - Find the sine of all the numbers in d
d_sin = np.sin(d)
print(d_sin)
# Exercise 2 - Find the cosine of all the numbers in d
d_cos = np.cos(d)
# Exercise 3 - Find the tangent of all the numbers in d
d_tan = np.tan(d|)
# Exercise 4 - Find all the negative numbers in d
d_neg = d[d < 0]
print(d_neg)
# Exercise 5 - Find all the positive numbers in d
d_pos = d[d > 0]
# Exercise 6 - Return an array of only the unique numbers in d.
unique_d = np.unique(d)
# Exercise 7 - Determine how many unique numbers there are in d.
u_count_d = len(unique_d)
print(u_count_d)
# Exercise 8 - Print out the shape of d.
print(d.shape)
# Exercise 9 - Transpose and then print out the shape of d.
transposed_d = d.transpose()
print(transposed_d.shape)
# Exercise 10 - Reshape d into an array of 9 x 2
d_9_2 = d.reshape(9, 2)
print(d_9_2)