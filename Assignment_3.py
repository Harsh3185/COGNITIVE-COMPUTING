#       1
import pandas 

data = {
    "Tid": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Refund": ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "No"],
    "Marital Status": ["Single", "Married", "Single", "Married", "Divorced", "Married", "Divorced", "Single", "Married", "Single"],
    "Taxable Income": ["125K", "100K", "70K", "120K", "95K", "60K", "220K", "85K", "75K", "90K"],
    "Cheat": ["No", "No", "No", "No", "Yes", "No", "No", "Yes", "No", "Yes"]
}

df = pandas.DataFrame(data)
print("Dataframe : \n" , df)

#       2

print("Rows 0,4,7,8 : \n" , df.loc[[0,4,7,8]])
print("\n")

#       3
print("Row from index 3 to 7: \n" ,df.iloc[3:8])
print("\n")
print("Row from index 4 to 8, and column 2 to 4:\n " ,df.iloc[4:9 , 2:5])
print("\n")
print("All rows with column index 1 to 3 : \n" ,df.iloc[ : , 1:4])
print("\n")

#       4
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()


api.dataset_download_files('uciml/iris', path='datasets/', unzip=True)


df_csv = pandas.read_csv('datasets/Iris.csv')


print(df_csv.head())
print("\n")

#       5

df_csv.drop(3 , axis = 0, inplace= True)
print("After delete row 4 \n" , df_csv)
print("\n")

df_csv.drop(df_csv.columns[2], axis = 1, inplace= True)
print("After delete column 3 \n" , df_csv)
print("\n")

#       6
data = {
    'Employee_ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Edward'],
    'Department': ['HR', 'IT', 'IT', 'Marketing', 'Sales'],
    'Age': [29, 34, 41, 28, 38],
    'Salary': [50000, 70000, 65000, 55000, 60000],
    'Years_of_Experience': [4, 8, 10, 3, 12],
    'Joining_Date': ['2020-03-15', '2017-07-19', '2013-06-01', '2021-02-10', '2010-11-25'],
    'Gender': ['Female', 'Male', 'Male', 'Female', 'Male'],
    'Bonus': [5000, 7000, 6000, 4500, 5000],
    'Rating': [4.5, 4.0, 3.8, 4.7, 3.5]
}

df = pandas.DataFrame(data)
df.to_csv('employees.csv', index=False)
print("Dataset created : 'employees.csv'.")
print("\n")

df = pandas.read_csv('employees.csv')

#   a
print("(a)Shape of Dataframe : \n")
print(df.shape)
print("\n")

#   b
print("(b) Datatype  and non-null count of the DataFrame:")
print(df.info())
print("\n")

#c
print("(b) Describe statistics of the DataFrame:")
print(df.describe())
print("\n")

#d
print("(d) First 5 rows:  \n")
print(df.head())
print("\n")
print("    Last 3 rows:  \n")
print(df.tail(3))
print("\n")

#e
print("(e) Statistics:")
print(f"  Average salary: {df['Salary'].mean()}")
print(f"  Total bonus: {df['Bonus'].sum()}")
print(f"  Youngest employee's age: {df['Age'].min()}")
print(f"  Highest performance rating: {df['Rating'].max()}")
print("\n")

#f
sorted_df = df.sort_values(by='Salary', ascending=False)
print("\n(f) Sorted by Salary in descending order: \n")
print(sorted_df)
print("\n")

#g
def performance_rating(rating):
    if rating >= 4.5:
        return 'Excellent'
    elif 4.0 <= rating < 4.5:
        return 'Good'
    else:
        return 'Average'
    

df['Performance'] = df['Rating'].apply(performance_rating)
print("(g) Dataframe with Performance rating: \n")
print(df)
print("\n")

#h
print("(h) Missing values in the DataFrame:")
print(df.isnull().sum())
print("\n")

#i
df.rename(columns={'Employee_ID': 'ID'}, inplace=True)
print("(i) Renamed DataFrame: \n")
print(df)
print("\n")

#j
filtered_df = df[(df['Years_of_Experience'] > 5)]
print("(j) More than 5 years of experience: \n")
print("\n")
filtered_df = df[(df['Department']  == 'IT')]
print("    IT department: \n")
print(filtered_df)
print("\n")

#k
print("(k) Dataset with Tax column:")
df['Tax'] = df['Salary'] * 0.1
print(df)
print("\n")

#l
df.to_csv('modified_employees.csv', index=False)
print("(l) Modified DataFrame saved as 'modified_employees.csv'.")
print("\n")

