from pydataset import data
import pandas as pd
import numpy as np

np.random.seed(123)
students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']
# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))
df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

# A. Create a column named passing_english that indicates whether each student has a passing grade in english.
df['passing_english'] = df.english > 70
# B. Sort the english grades by the passing_english column. How are duplicates handled?
df.sort_values(by='english')
# It is done by the value first and then based on the normal index number.
# C. Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)
df.sort_values(by='name').sort_values(by='english')
df.sort_values(by= ['english', 'name'])
# D. Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.
df.sort_values(by='english').sort_values(by='passing_english')
# E. Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.
df['overall_grade'] = (df.math + df.english + df.reading)/3
df

mpg = data('mpg')
data('mpg', show_doc=True)
mpg
# 1. How many rows and columns are there?
# There are 234 rows and 11 columns
# 2. What are the data types of each column?
mpg.dtypes
# 3. Summarize the dataframe with .info and .describe
mpg.info()
mpg.describe()
# 4. Rename the cty column to city.
mpg = mpg.rename(columns={'cty': 'city'})
# 5. Rename the hwy column to highway.
mpg = mpg.rename(columns={'hwy': 'highway'})
# 6. Do any cars have better city mileage than highway mileage?
mpg[mpg.city > mpg.highway]
# No
# 7. Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
mpg['mileage_difference'] = mpg.highway - mpg.city
# 8. Which car (or cars) has the highest mileage difference?
mpg.sort_values(by='mileage_difference', ascending=False)
# Honda Civic and Volkswagen New Beetle
# 9. Which compact class car has the lowest highway mileage? The best?
mpg[mpg['class'] == 'compact'].sort_values(by='highway')
# Lowest: Volkswagen Jetta, Best: Volkswagen Jetta (4 cyl manual)
# 10. Create a column named average_mileage that is the mean of the city and highway mileage.
mpg['average_mileage'] = (mpg.highway + mpg.city) / 2
# 11. Which dodge car has the best average mileage? The worst?
mpg[mpg.manufacturer == 'dodge'].sort_values(by='average_mileage')
# Best: caravan 2wd
# Worst: ram 1500 pickup 4wd, durango, dakota pickup 4wd

Mammals = data('Mammals')
data('Mammals', show_doc=True)

# 1. How many rows and columns are there?
# 107 rows and 4 columns
# 2. What are the data types?
Mammals.dtypes
# 3. Summarize the dataframe with .info and .describe
Mammals.info()
Mammals.describe()
# 4. What is the the weight of the fastest animal?
Mammals.sort_values(by=['speed', 'weight'])
# 55 Kgs
Mammals.sort_values(by='weight').sort_values(by='speed', ascending=False)
# 5. What is the overall percentage of specials?
Mammals.specials.sum() / len(Mammals) * 100 
# 9.35% 
# 6. How many animals are hoppers that are above the median speed? What percentage is this?
Mammals.hoppers[Mammals.hoppers & (Mammals.speed > Mammals.speed.median())].sum() / len(Mammals) * 100
# 7 total, 6.54%

