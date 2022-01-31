import pandas as pd
from env import host, user, password
def get_db_url(username=user, hostname=host, password=password, db_name):
    url = f'mysql+pymysql://{username}:{password}@{host}/{db_name}'
    return url
url = get_db_url(user, host, password, 'employees')

pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)
# 5. A. With a typo on the db_name I got a access denied error (Operational Error)
# 5. B. With an error in SQL syntax I got back a SQL like error (Operational Error), that said
# 'no tables used'
employees = pd.read_sql('SELECT * FROM employees', url)
titles = pd.read_sql('SELECT * FROM titles', url)
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

