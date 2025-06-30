# import pyodbc 
# import os

# connection = pyodbc.connect('DRIVER={SQL Server};'+
#                           'Server=DESKTOP-LCNFE94\SQLEXPRESS;'+ 
#                           'Database=HMS;'+
#                           'Trusted_Connection=True')

# # connection.autocommit = True
# print("Connected to database")

#### *************************************
# cursor = connection.cursor()

# os.system("cls") # to clear output screen

# connection.execute("insert into Mytab values ('AliHassan', 24)")
# connection.execute("update Mytab set Age=8 where Name='Wali'")
# cursor.execute("select * from Mytab")

# for data in cursor:
#     print(data[0], data[1])

