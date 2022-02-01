import pandas as pd
import numpy as np
from env import host, user, password
from env import get_db_url

def get_db_url(username=user, hostname=host, password=password, db_name):
    url = f'mysql+pymysql://{username}:{password}@{host}/{db_name}'
    return url
e_url = get_db_url('employees')

# Part I

pd.read_sql('SELECT * FROM employees', e_url)
# 5. A. With a typo on the db_name I got a access denied error (Operational Error)
# 5. B. With an error in SQL syntax I got back a SQL like error (Operational Error), that said
# 'no tables used'
employees = pd.read_sql('SELECT * FROM employees', e_url)
titles = pd.read_sql('SELECT * FROM titles', e_url)
employees # 300024 rows, 6 columns
titles # 443308 rows, 4 columns
# There are more rows in these than reside on the database in Sequel Ace currently
employees.describe()
employees.info()
titles.describe()
titles.info()
# 9. How many unique titles are there
titles.nunique()
# There are 7 unique titles
# 10. What is the oldest date in the to_date column?
oldest_date = pd.read_sql('SELECT to_date FROM titles ORDER BY to_date', url)
oldest_date.head()
# 1985-03-01
# 11. What is the most recent date in the to_date column?
oldest_date.tail()
# 9999-01-01

# Part II

# 1. Copy the users and roles DataFrames from the examples above.
users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
# 2. What is the result of using a right join on the DataFrames?
users.merge(roles, left_on='role_id', right_on='id', how='right', indicator=True)
# 3. What is the result of using an outer join on the DataFrames?
users.merge(roles, left_on='role_id', right_on='id', how='outer', indicator=True)
# 4. What happens if you drop the foreign keys from the DataFrames and try to merge them?
# It will still allow you to perform the merges, but the values may not add up correctly (they likely will not)
# dropping the foreign key and then merging on a different key will cause data inaccurately represent both tables
# the example in class shows where the id get matched up and now the wrong role is assigned.
# 5. Load the mpg dataset from PyDataset.
from pydataset import data
mpg = data('mpg')
# 6. Output and read the documentation for the mpg dataset.
data('mpg', show_doc=True)
# 7. How many rows and columns are in the dataset?
# 234 rows, 11 columns
# 8. Check out your column names and perform any cleanup you may want on them.
mpg = mpg.rename(columns={'cty': 'city', 
                          'hwy': 'highway'})
# 9. Display the summary statistics for the dataset.
mpg.info()
mpg.describe()
# 10. How many different manufacturers are there?
mpg.nunique()
# There are 15 different manufacturers
# 11. How many different models are there?
# There are 38 different models.
# 12. Create a column named mileage_difference like you did in the 
# DataFrames exercises; this column should contain the difference between highway and city mileage 
# for each car.
mpg['mileage_difference'] = mpg.highway - mpg.city
# 13. Create a column named average_mileage like you did in the DataFrames exercises; this is the mean 
# of the city and highway mileage.
mpg['average_mileage'] = mpg[['city', 'highway']].mean(axis=1)
# 14. Create a new column on the mpg dataset named is_automatic that holds boolean values denoting 
# whether the car has an automatic transmission.
mpg['is_automatic'] = mpg.trans.str.contains('auto')
# 15. Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?
mpg.groupby('manufacturer').average_mileage.max().sort_values(ascending = False)
# Volkswagen
# 16. Do automatic or manual cars have better miles per gallon?
mpg.groupby('is_automatic').average_mileage.max().sort_values(ascending = False)
# Manual 

# Part III
# 1. Use your get_db_url function to help you explore the data from the chipotle database.
c_url = get_db_url('chipotle')
# 2. What is the total price for each order?
c_orders = pd.read_sql('SELECT * FROM orders', c_url)
c_orders['price_f'] = c_orders.item_price.str.replace('$', '').astype('float')
c_orders['total_i'] = c_orders.price_f * c_orders.quantity
price_per_order = c_orders.groupby('order_id').sum('total_i')
price_per_order
# 3. What are the most popular 3 items?
c_orders.groupby('item_name').sum('quantity').sort_values(by='quantity', ascending = False).head(3)
# Chicken bowl, Chicken burrito, Chips and Guac
# 4. Which item has produced the most revenue?
c_orders.groupby('item_name').sum('total_i').sort_values(by='total_i', ascending = False).head(1)
# Chicken bowl, $8044.63
# 5. Join the employees and titles DataFrames together.
e_url = get_db_url('employees')
employees = pd.read_sql('SELECT * FROM employees', e_url)
titles = pd.read_sql('SELECT * FROM titles', e_url)
emp_titles = employees.merge(titles, how='outer', left_on='emp_no', right_on='emp_no')
# 6. For each title, find the hire date of the employee that was hired most recently with that title.
emp_titles.groupby('title').hire_date.max()
# 7. Write the code necessary to create a cross tabulation of the number of titles by department. 
# (Hint: this will involve a combination of SQL code to pull the necessary data and python/pandas 
# code to perform the manipulations.)
departments = pd.read_sql('SELECT * FROM departments', e_url)
dept_emp = pd.read_sql('SELECT * FROM dept_emp', e_url)
dept_emp
emp_title_dept_emp = emp_titles.merge(dept_emp, how='outer', left_on='emp_no', right_on='emp_no')|
emp_title_dept_emp
all_things = emp_title_dept_emp.merge(departments, how='outer', left_on='dept_no', right_on='dept_no')
emp_title_dept_emp
pd.crosstab(all_things.dept_name, all_things.title, margins=True)


dept_title_query = '''
    SELECT t.emp_no,
    t.title,
    t.from_date,
    t.to_date,
    d.dept_name
    from departments AS d
    JOIN dept_emp AS de USING(dept_no) 
    JOIN titles AS t USING(emp_no);
'''
all_titles_crosstab = pd.crosstab(dept_titles.dept_name, dept_titles.title)
all_titles_crosstab

current_titles = dept_titles[dept_title.to_date == dept_titles.to_date.max()]
current_titles_crosstab = pd.crosstab(current_titles.dept_name, current_titles.title)
current_titles_crosstab.style.highlight_max(axis=1)