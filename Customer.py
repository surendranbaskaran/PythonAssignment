#Import Modules
import pandas as Pd
import pyodbc
import json
import time
import pip._vendor.requests
#read online API file
url="https://gorest.co.in/public/v2/users"
resp = pip._vendor.requests.get(url=url)
jsonData = resp.json()
#print(jsonData)
#establish SQL connection
server = 'DESKTOP-PM73NEM' 
database = 'study' 
username = 'sa' 
password = 'Su235190' 
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()
for i, item in enumerate (jsonData):
    strQuery="insert into dbo.users values('"+str(item['id'])+"','" +item['name']+"','"+item['email']+"','"+item['gender']+"','"+item['status']+"')"
    cursor.execute(strQuery)
    conn.commit()
#Export .csv file
sql_query = Pd.read_sql_query('''select * from dbo.users''',conn) # here, the 'conn' is the variable that contains your database connection information from step 2
df = Pd.DataFrame(sql_query)
filename = 'C:\Suren Python\CustAPI\Target\exported_data' + time.strftime("%Y%m%d-%H%M%S") +'.csv'
df.to_csv (filename, index = False) # place 'r' before the path name
conn.close()