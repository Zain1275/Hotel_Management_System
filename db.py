import pyodbc 
import os

def get_connection():
    connection = pyodbc.connect(
        'DRIVER={SQL Server};'
        'Server=DESKTOP-LCNFE94\\SQLEXPRESS;'
        'Database=HMS;'
        'Trusted_Connection=True'
    )
    connection.autocommit = True
    return connection

# connection = pyodbc.connect('DRIVER={SQL Server};'+
#                           'Server=DESKTOP-LCNFE94\SQLEXPRESS;'+ 
#                           'Database=HMS;'+
#                           'Trusted_Connection=True')

# connection.autocommit = True
# print("Connected to database")
# cursor = connection.cursor()

#### *************************************

os.system("cls") # to clear output screen

# # connection.execute("insert into Mytab values ('AliHassan', 24)")
# # connection.execute("update Mytab set Age=8 where Name='Wali'")
# # cursor.execute("select * from Department")


# # for data in cursor:
# #     print( data)


# class Customer: #**************************
#     id =0 
#     name = "no name"
#     password = "0000"

#     def __init__(self, id=0, n="Unknown", p="0"):
#         self.id = id
#         self.name= n
#         self.password = p

#     def show(self):
#         print(self.id, self.name, self.password)

# custlist = []



# ## sending data to sql table from a list *********************************

# custlist.append(Customer(0, "zain", "11"))
# custlist.append(Customer(1, "wali", "22"))

# for c in custlist:
#     cursor.execute(
#         "INSERT INTO Customer (custId, custName, custPassword) VALUES (?, ?, ?)",
#         c.id, c.name, c.password
#     )
# print("Command run succesfully")

# # *******************************


# ## getting data from sql table in a list ******************************

# custlist.clear()

# cursor.execute("SELECT * FROM Customer")
# rows = cursor.fetchall()

# for row in rows:
#     custlist.append(Customer(row[0], row[1], row[2]))

# print("Customer list loaded from database:\n")
# for c in custlist:
#     c.show()

# # ****************************



# class Room: #***************************************
#     id = 0 
#     type=  ""
#     status = True
#     cust_id = None

#     def __init__(self, i, t, st, cid = None):
#         self.id = i
#         self.type = t
#         self.status = st
#         self.cust_id = cid

#     def show(self):
#         print(f"{self.id}  {self.type}  {self.status}  {self.cust_id}")


# roomList = []

# sending data to database*********************

# roomList.append(Room(2, "A", False))
# # custlist.append(Customer(1, "wali", "22"))

# for r in roomList:
#     cursor.execute(
#         "insert into Room (roomId, roomType, isAvailable, custId) values (?, ?, ?, ?)",
#         r.id, r.type, r.status, r.cust_id
#     )
# print("Command run succesfully")


# receiving data from database  ******************

# roomList.clear()

# cursor.execute("SELECT * FROM Room")
# rows = cursor.fetchall()

# for row in rows:
#     roomList.append(Room(row[0], row[1], row[2], row[3]))

# print("Rooms list loaded from database:\n")
# for c in roomList:
#     c.show()
# print("Command run succesfully")
