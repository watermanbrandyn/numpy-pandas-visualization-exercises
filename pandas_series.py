import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Part I
fruits =     ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato",
 "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

fruits = pd.Series(fruits)
# 1. Determine the number of elements in fruits.
fruits.size
# There are 17 elements in fruits.
# 2. Output only the index from fruits.
fruits.index
# RangeIndex(start=0, stop=17, step=1)
# 3. Output only the values from fruits.
fruits.values
# 4. Confirm the data type of the values in fruits.
fruits.dtype
# 5. Output only the first five values from fruits. Output the last three values. Output two random values from fruits.
fruits.head(5)
fruits.tail(3)
fruits.sample(2)
# 6. Run the .describe() on fruits to see what information it returns when called on a Series with string values.
fruits.describe()
# 7. Run the code necessary to produce only the unique string values from fruits.
fruits.unique()
# 8. Determine how many times each unique string value occurs in fruits.
fruit_values = fruits.value_counts()
# 9. Determine the string value that occurs most frequently in fruits.
# This is 'kiwi' as seen from above command (4 times)
fruit_values.nlargest(n=1, keep='all')
# 10. Determine the string value that occurs least frequently in fruits.
fruit_values.nsmallest(n=1, keep='all')

# Part II
# 1. Capitalize all the string values in fruits.
fruits.str.capitalize()
# 2. Count the letter "a" in all the string values (use string vectorization).
fruits.str.count('a')
# 3. Output the number of vowels in each and every string value.
vowels = list('aeiouAEIOU')
fruits.str.count('[aeiou]')
# 4. Write the code to get the longest string value from fruits.
max(fruits, key = len)
# 5. Write the code to get the string values with 5 or more letters in the name.

# 6. Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.
fruits.apply(lambda)
# 7. Write the code to get only the string values containing the substring "berry".

# 8. Write the code to get only the string values containing the substring "apple".

# 9. Which string value contains the most vowels?

# Part III
letters = list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')
letters = pd.Series(letters)

# 1. Which letter occurs the most frequently in the letters Series?
letters.value_counts()
# The letter 'y'
# 2. Which letter occurs the Least frequently?
# The letter 'l'
# 3. How many vowels are in the Series?

# 4. How many consonants are in the Series?

# 5. Create a Series that has all of the same letters but uppercased.

# 6. Create a bar plot of the frequencies of the 6 most commonly occuring letters.

