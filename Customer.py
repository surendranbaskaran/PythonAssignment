from ast import Return
from distutils.log import debug
import os,json
import pydoc
import string
import pandas as Pd
from click import open_file
from colorama import Cursor
import pyodbc
#read Json file
file1 = os.path.abspath('C:\Suren Python\CustAPI\JSON\Employee.json')
json_data=open_file(file1).read()
json_obj=json.loads(json_data)
#print(json_obj)
#establish SQL connection
server = 'DESKTOP-PM73NEM' 
database = 'study' 
username = 'sa' 
password = 'Su235190' 
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()
Employee = json_obj['Employees']
for i, item in enumerate (Employee):
    strQuery="insert into dbo.employees values('"+item['userId']+"','" +item['jobTitle']+"','"+item['firstName']+"','"+item['lastName']+"','"+item['employeeCode']+"','"+item['region']+"','"+item['phoneNumber']+"','"+item['emailAddress']+"')"
    cursor.execute(strQuery)
    conn.commit()
#Export .csv file
sql_query = Pd.read_sql_query('''select * from dbo.employees''',conn) # here, the 'conn' is the variable that contains your database connection information from step 2
df = Pd.DataFrame(sql_query)
df.to_csv (r'C:\Suren Python\CustAPI\Target\exported_data.csv', index = False) # place 'r' before the path name
conn.close()