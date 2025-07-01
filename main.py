import os
from db import get_connection

class Customer: #**************************
    id =0 
    name = "no name"
    password = "0000"

    def __init__(self, id=0, n="Unknown", p="0"):
        self.id = id
        self.name= n
        self.password = p

    def show(self):
        print(self.id, self.name, self.password)

class Manager:  #*********************************
    id =0 
    name = "no name"
    password = "0000"


    def __init__(self, id=0, n="Unknown", p="0"):
        self.id = id
        self.name= n
        self.password = p

    def show(self):
        print(self.id, self.name, self.password)



class Room: #***************************************
    id = 0 
    type =  ""
    status = True
    cust_id = None

    def __init__(self, i, t, st, cid):
        self.id = i
        self.type = t
        self.status = st
        self.cust_id = cid

    def show(self):
        print(f"{self.id}  {self.type}  {self.status}  {self.cust_id}")


class Booking:
    booking_id= 0
    cust_id = 0 
    room_id= 0

    def __init__(self,bid,  cid, rid):
        self.booking_id = bid
        self.cust_id = cid
        self.room_id = rid
    def show(self):
        print(f"{self.booking_id} {self.cust_id} {self.room_id}")

class Application:
    app_id = 0
    cust_id = 0
    room_id = 0
    app_status = None

    def __init__(self, apid, csid, rmid, app_status = None):
        self.app_id = apid
        self.cust_id=  csid
        self.room_id=  rmid
        self.app_status = app_status

    def showApplication(self):
        print("---------------")
        print(f"Application ID: {self.app_id}")
        print(f"Customer Id: {self.cust_id}")
        print(f"Room ID: {self.room_id}")
        if self.app_status == None:
            print(f"Application Status: Pending")
        elif self.app_status == False:
            print(f"Application Status: Rejected")
        elif self.app_status == True:
            print(f"Application Status: Approved")
        print("---------------")


class HMS:
    Roomlist = []
    Bookings=  []
    Applications = []
    def __init__(self):
        pass 
        # self.Roomlist.append(Room(101, "A", True, None))
        # self.Roomlist.append(Room(102, "A", True, None))
        # self.Roomlist.append(Room(103, "A", True, None))
        # self.Roomlist.append(Room(104, "A", True, None))
        # self.Roomlist.append(Room(201, "B", True, None))
        # self.Roomlist.append(Room(202, "B", True, None))

    def RoomsDetail(self):
        os.system("cls")
        print("ID Type Available Customer")
        for r in self.Roomlist:
            r.show()
        return 
    
    def displayAllApplication(self):
        for app in self.Applications:
            app.showApplication()


    def makeBooking(self, cid, rid):  # make only booking request/application
        for r in self.Roomlist:
            if r.id == rid and r.status == True:
                # tempint = self.Bookings.__len__()
                # self.Bookings.append(Booking(tempint, cid, rid))
                tempint = self.Applications.__len__()
                self.Applications.append(Application(tempint, cid, rid))
                r.status = False
                r.cust_id = cid 
                return
            elif r.id == rid and r.status == False:
                print("Room not available..!!") 
                input("Enter any key to continue..!!")
                return
        print("Room Does not exist.. !!")
        input("Enter any key to continue..!!")
        return
    
    def approveBooking(self, cid , rid): # when application approved by manager. booking placed 
        tempint = self.Bookings.__len__()
        self.Bookings.append(Booking(tempint, cid, rid)) 
         
    
    def showApplicationStatus(self, cid):
        for b in self.Applications:
            if b.cust_id == cid:
                b.showApplication()
        return
    
    def manageApplications(self):
        tempint = int(input("Enter Application No: "))
        for a in self.Applications:
            if a.app_id == tempint:
                temp = ""
                temp = input("Enter Command : (Approved/A , Reject/R) ")
                if temp == "A" or temp == "a":
                    a.app_status = True
                    print("Action Preformed..!!")
                    return a.cust_id, a.room_id
                elif temp == "r" or  temp == "R": 
                    a.app_status = False
                    print("Action Preformed..!!")
                    return None, a.room_id
                else:
                    print("Invalid Input..!!")  
                    return None, None

        print("Application Does not exist..!!")
        return None, None

    
    def showbookings(self):
        print("BookingId  CustomerId  Room-No")
        for b in self.Bookings:
            b.show()

    def clearRoom(self, rid):
        for r in  self.Roomlist:
            if rid == r.id:
                r.status = True
                r.cust_id = None



def signIn(tlist):  # accessing old account 
    temp = input("Enter Username: ")
    tempint= 0
    for m in tlist:
        if m.name == temp:
            tempint = 1
            temp1 = input("Enter Password: ")
            if m.password == temp1: 
                print("Login Successfully..!")
                tempint = m.id
                temp = m.name
                input("Press any key to continue..!!")
                return True , tempint, temp 
            else:
                print("Password is invalid..!!")
                input("Press any key to continue..!!")
                return False , None, None

    if tempint == 0:
        print("User Not found..!!")
        input("Press any key to continue..!!")
        return False, None, None

def signUpCustomer(t, tlist):  # account creation 
    temp = input("Enter name: ")
    temp2 = input("Enter Password: ")
    tempint = tlist.__len__()
    # t.register(tempint, temp, temp2)
    tlist.append(Customer(tempint, temp, temp2))
    print("signup successfully ", end=" ")
    tlist[tempint].show()
    input("press key to continue..!!") 

def signUpManager(t, tlist):  # account creation 
    temp = input("Enter name: ")
    temp2 = input("Enter Password: ")
    tempint = tlist.__len__()
    # t.register(tempint, temp, temp2)
    tlist.append(Manager(tempint, temp, temp2))
    print("signup successfully ", end=" ")
    tlist[tempint].show()
    input("press key to continue..!!") 

def custmenu(custid, custname): # customer menu
    while(True):
        os.system("cls")
        print(f"Hotel Management System (Customer) -- Id:{custid} Username:{custname}")
        print("1. Rooms Detail")
        print("2. Book Room")
        print("3. Booking Status")
        # print("4. Payment/Bill")
        print("0. Back")

        choice = int(input("Enter Choice: "))
        match(choice):
            case 0:
                return
            case 1 :
                hms.RoomsDetail()
                input("press any key to continue..!!")
            case 2 :
                tempint = int(input("Enter Room No: "))
                hms.makeBooking(custid, tempint) # sending customer id and room number 
                pass
            case 3 :
                hms.showApplicationStatus(custid)
                input("Press any key to continue..!!")
            
        

def managMenu(managid, managname): # Manager's menu
    while(True):
        os.system("cls")
        print(f"Hotel Management System (Manager) -- Id:{managid} Username:{managname}")
        print("1. Rooms Detail")
        print("2. Show All Bookings ")
        print("3. Show Booking Applications")
        print("4. Manage Applications")
        print("0. Back")

        choice = int(input("Enter Choice: "))
        match(choice):
            case 0:
                return
            case 1 :
                hms.RoomsDetail()
                input("press any key to continue..!!")
            case 2:
                hms.showbookings()
                input("press any key to continue..!!")
            case 3 :
                hms.displayAllApplication()
                input("press any key to continue..!!")
                pass
            case 4 :
                tempint, temp = hms.manageApplications() # taking customer id and room id 
                if tempint != None and temp != None: # if room approved then this will run 
                    hms.approveBooking(tempint, temp)
                elif tempint == None :
                    hms.clearRoom(temp) # giving room id to make it free 
                input("press any key to continue..!!")
                pass


def login():
    os.system("cls")
    print("1. SignIn")
    print("2. SignUp")
    print("3. Show Users")
    print("0. Back")
    ch = int(input("Enter Choice: "))
    return ch

def onLoad(cursor, custlist, managlist, hms): # load all data from database to lists 

    # getting customer data form database 
    custlist.clear()
    cursor.execute("SELECT * FROM Customer")
    rows = cursor.fetchall()

    for row in rows:
        custlist.append(Customer(row[0], row[1], row[2]))

    # getting manager's data from database 
    managlist.clear()
    cursor.execute("SELECT * FROM Manager")
    rows = cursor.fetchall()

    for row in rows:
        managlist.append(Manager(row[0], row[1], row[2]))

    # getting rooms data 
    hms.Roomlist.clear()
    cursor.execute("SELECT * FROM Room")
    rows = cursor.fetchall()

    for row in rows:
        hms.Roomlist.append(Room(row[0], row[1], row[2], row[3]))

    # getting Applications data 
    hms.Applications.clear()
    cursor.execute("SELECT * FROM Applications")
    rows = cursor.fetchall()

    for row in rows:
        hms.Applications.append(Application(row[0], row[1], row[2], row[3]))

    # getting Bookings data 
    hms.Bookings.clear()
    cursor.execute("SELECT * FROM Bookings")
    rows = cursor.fetchall()

    for row in rows:
        hms.Bookings.append(Booking(row[0], row[1], row[2]))

    
    


def onExit(cursor, custlist, managlist, hms): # send data from lists to database 
    

    cursor.execute("delete from Bookings")
    cursor.execute("delete from Applications")
    cursor.execute("delete from Room")
    cursor.execute("delete from Customer")
    cursor.execute("delete from Manager")


    # sending customer's data 
    for c in custlist:
        cursor.execute(
            "INSERT INTO Customer (custId, custName, custPassword) VALUES (?, ?, ?)",
            c.id, c.name, c.password
        )

    # sending Manager's data 
    for c in managlist:
        cursor.execute(
            "INSERT INTO Manager (managId, managName, managPassword) VALUES (?, ?, ?)",
            c.id, c.name, c.password
        )

    # sending Room's data 
    for r in hms.Roomlist:
        cursor.execute(
            "INSERT INTO Room (roomId, roomType, isAvailable, custId) VALUES (?, ?, ?, ?)",
            r.id, r.type, r.status, r.cust_id
        )
    
    # sending Application's data 
    for a in hms.Applications:
        cursor.execute(
            "INSERT INTO Applications (appId, custId, roomId, appStatus) VALUES (?, ?, ?, ?)",
            a.app_id, a.cust_id, a.room_id, a.app_status
        )

    # sending Booking's data 
    for a in hms.Bookings:
        cursor.execute(
            "INSERT INTO Bookings (bookingId, custId, roomId) VALUES (?, ?, ?)",
            a.booking_id, a.cust_id, a.room_id
        )
##### Main Function ########


conection = get_connection()
cursor = conection.cursor()

choice = 0 
temp= ""
temp1 = ""
tempint = 0
tempbool = None
custlist = []
managlist = []
cust = Customer()
manag = Manager()
hms = HMS()


onLoad(cursor, custlist, managlist, hms)

while(True):
    os.system("cls")

    print("Hotel Management System")
    print("1. Manager")
    print("2. Customer")
    print("0. Exit")
    choice = int(input("Enter Choice: "))

    if choice == 0:
        onExit(cursor, custlist, managlist, hms)
        exit()
    elif choice == 1:  ## manager login
        choice = login()
        match(choice):
            case 0 : ## back
                exit()
            case 1 : ## signIN old account
                tempbool, tempint, temp = signIn(managlist)

                if tempbool == True: # signin successfull manager 
                    managMenu(tempint, temp) # sending manager  id and username 


            case 2: ## signUp  ** create account
                signUpManager(manag, managlist)
            case 3:
                for m in managlist:
                    m.show()
                input("Press any key to continue..!!")

    elif choice == 2:  ## customer login
        choice = login()
        match(choice):
            case 0 : ## back
                exit()
            case 1 : ## signIN old account
                tempbool, tempint, temp = signIn(custlist)
                
                if tempbool == True: # signin successfull customer 
                    custmenu(tempint, temp) # sending customer id and username 
                    
            case 2: ## signUp ** create account
                signUpCustomer(cust, custlist)
            case 3:
                for c in custlist:
                    c.show()
                input("Press any key to continue..!!")
    else:
        print("Invalid Input..!!")
        input("Press any key to Continue..!!")