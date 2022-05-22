from tkinter import *
import sqlite3                                                         # Imports SQL commands
from tkinter import messagebox


#--------------------------- Creating the window "Warwick IT hub" ------------------------------
root = Tk()
root.title('Warwick IT hub')                                           # Assigning window name
img = Image("photo", file="~/app-icon.png")                            # Icon for the GUI created
root.call('wm','iconphoto', root._w, img)

frame = LabelFrame(root, padx=250, pady=250)                           # A frame of size 250x250 for the window
frame.pack(padx=10, pady=10)


#----------------------- Function definitions for each button clicked --------------------------
def onClick():
    top  = Tk()                                                         # New window on click 
    top.title('Warwick IT hub - Room Details')                          # Assigning the title "Warwick IT hub - Room details"
    fr = LabelFrame(top, text = 'Display rooms:', padx = 250, pady = 250)
    fr.pack(padx = 10, pady = 10)

    def b1topF():                                                       # Button definition for searching by capacity
        capL = Label(fr, text = 'Enter the minimum capacity required:') # Defining the text label
        capL.grid(row = 1, column = 0)

        capB = Entry(fr, width = 30)                                    # Enter the capacity as integer 
        capB.grid(row = 1, column = 1)

        def subC():
            temp = Tk()                                                 # Temporary window created to display the file contents, window {"temp"}
            temp.title('Warwick IT hub - By Capacity')                  # Assigning window title "Warwick IT hub - By capacity"
            connect = sqlite3.connect('rooms.db')                       # Opening the file by assigning it to the variable - {"connect"}, file name - {"rooms.db"}
            cur = connect.cursor()                                      # Executing a cursor onto the file
            cur.execute('SELECT * FROM rooms WHERE capacity >=' + capB.get())   # Executing the SQL query on the database opened
            rec = cur.fetchall()                                        # All the rows with capacity more than the entered capacity is fetched here
            p_recid = ''
            p_recbuild = ''
            p_recname = ''
            p_reccap = ''
            p_rectyp = ''
            p_recfac = '' 
            p_rectim = ''
            p_recbook = ''                                              # Declaration of variables as NULL values 
            for r in rec:                                               # Going through all the fetched data
                p_recid += str(r[0]) + '\n'                             # 'ID' is the First element
                p_recbuild += str(r[1]) + '\n'                          # 'Building' is the Second element
                p_recname += str(r[2]) + '\n'                           # 'Name' is the Third element
                p_reccap += str(r[3]) + '\n'                            # 'Capacity' is the Fourth element
                p_rectyp += str(r[4]) + '\n'                            # 'Type' is the Fifth element
                p_recfac += str(r[5]) + '\n'                            # 'Facilities' is the Sixth element
                p_rectim += str(r[6]) + '\n'                            # 'Time_availability' is the Seventh element
                p_recbook += str(r[7]) + '\n'                           # 'Booked' is the Eigth element
                                                                        # Assigning the values in the file into the null variables created
            

            # -------------------- Displaying the values as a table in the GUI window -------------------
            disp = Label(temp, text = "ID")                             # Label text on row 1 column 0
            disp.grid(row = 1, column = 0)                              
            disL = Label(temp, text = p_recid)                          # Values acquired from the file disaplyed in table format starting from row 2 column 0
            disL.grid(row = 2, column = 0)

            disp = Label(temp, text = "Capacity")                       # Label text on row 1 column 1
            disp.grid(row = 1, column = 1)
            disL = Label(temp, text = p_reccap)                         # Values acquired from the file disaplyed in table format starting from row 2 column 1
            disL.grid(row = 2, column = 1)

            disp = Label(temp, text = "Building")                       # Label text on row 1 column 2
            disp.grid(row = 1, column = 2)
            disL = Label(temp, text = p_recbuild)                       # Values acquired from the file disaplyed in table format starting from row 2 column 2
            disL.grid(row = 2, column = 2)

            disp = Label(temp, text = "Room Name")                      # Label text on row 1 column 3
            disp.grid(row = 1, column = 3)
            disL = Label(temp, text = p_recname)                        # Values acquired from the file disaplyed in table format starting from row 2 column 3
            disL.grid(row = 2, column = 3)

            disp = Label(temp, text = "Type")                           # Label text on row 1 column 4
            disp.grid(row = 1, column = 4)
            disL = Label(temp, text = p_rectyp)                         # Values acquired from the file disaplyed in table format starting from row 2 column 4
            disL.grid(row = 2, column = 4)

            disp = Label(temp, text = "Facilities")                     # Label text on row 1 column 5
            disp.grid(row = 1, column = 5)
            disL = Label(temp, text = p_recfac)                         # Values acquired from the file disaplyed in table format starting from row 2 column 5
            disL.grid(row = 2, column = 5)

            disp = Label(temp, text = "Availability")                   # Label text on row 1 column 6
            disp.grid(row = 1, column = 6)
            disL = Label(temp, text = p_rectim)                         # Values acquired from the file disaplyed in table format starting from row 2 column 6
            disL.grid(row = 2, column = 6)

            disp = Label(temp, text = "Booking")                        # Label text on row 1 column 7
            disp.grid(row = 1, column = 7)
            disL = Label(temp, text = p_recbook)                        # Values acquired from the file disaplyed in table format starting from row 2 column 7
            disL.grid(row = 2, column = 7)

            connect.commit()                                            # Committing the changes made in the file
            connect.close()                                             # Closing the file

            def closeBF():                                              # An exit button to close the window {"temp"}
                temp.destroy()                                          # Statement to close the window

            closeB = Button(temp, text = 'Exit', command = closeBF)     # Button "Exit" to close the window {"temp"}
            closeB.grid(row = 0, column = 0)

        sub = Button(fr, text = 'Search', command = subC)               # Button to search by capacity by calling the function {"subC"}
        sub.grid(row = 2, columnspan = 2)

    def b2topF():                               
        temp = Tk()                                                     # Window to display file contents by availability, file name - {"rooms.db"}
        temp.title('Warwick IT hub - By Availability')                  # Assigning title "Warwick IT hub - By Availability" to the new window
        connect = sqlite3.connect('rooms.db')                           # Opening the file {"rooms.db"} and assigning it to variable connect
        cur = connect.cursor()                                          # Assigning a cursor to browse through the file
        cur.execute('SELECT * FROM rooms WHERE booked = "Available"')   # Executing the query on the file to get values with booked value = "Available"
        rec = cur.fetchall()                                            # Fetching the values from the file and assigning it to variable {"rec"}
        p_recid = ''
        p_recbuild = ''
        p_recname = ''
        p_reccap = ''
        p_rectyp = ''
        p_recfac = '' 
        p_rectim = ''
        p_recbook = ''                                                  # Declaration of variables as NULL values 
        for r in rec:                                                   # Going through all the fetched data
            p_recid += str(r[0]) + '\n'                                 # 'ID' is the First element
            p_recbuild += str(r[1]) + '\n'                              # 'Building' is the Second element
            p_recname += str(r[2]) + '\n'                               # 'Name' is the Third element
            p_reccap += str(r[3]) + '\n'                                # 'Capacity' is the Fourth element
            p_rectyp += str(r[4]) + '\n'                                # 'Type' is the Fifth element
            p_recfac += str(r[5]) + '\n'                                # 'Facilities' is the Sixth element
            p_rectim += str(r[6]) + '\n'                                # 'Time_availability' is the Seventh element
            p_recbook += str(r[7]) + '\n'                               # 'Booked' is the Eigth element
                                                                        # Assigning the values in the file into the null variables created

        # -------------------- Displaying the values as a table in the GUI window -------------------
        disp = Label(temp, text = "ID")                                 # Label text on row 1 column 0
        disp.grid(row = 1, column = 0)
        disL = Label(temp, text = p_recid)                              # Values acquired from the file disaplyed in table format starting from row 2 column 0
        disL.grid(row = 2, column = 0)

        disp = Label(temp, text = "Availability")                       # Label text on row 1 column 1
        disp.grid(row = 1, column = 1)
        disL = Label(temp, text = p_rectim)                             # Values acquired from the file disaplyed in table format starting from row 2 column 1
        disL.grid(row = 2, column = 1)

        disp = Label(temp, text = "Booking")                            # Label text on row 1 column 2
        disp.grid(row = 1, column = 2)
        disL = Label(temp, text = p_recbook)                            # Values acquired from the file disaplyed in table format starting from row 2 column 2
        disL.grid(row = 2, column = 2)

        disp = Label(temp, text = "Building")                           # Label text on row 1 column 3
        disp.grid(row = 1, column = 3)
        disL = Label(temp, text = p_recbuild)                           # Values acquired from the file disaplyed in table format starting from row 2 column 3
        disL.grid(row = 2, column = 3)

        disp = Label(temp, text = "Room Name")                          # Label text on row 1 column 4
        disp.grid(row = 1, column = 4)
        disL = Label(temp, text = p_recname)                            # Values acquired from the file disaplyed in table format starting from row 2 column 4
        disL.grid(row = 2, column = 4)

        disp = Label(temp, text = "Type")                               # Label text on row 1 column 5
        disp.grid(row = 1, column = 5)
        disL = Label(temp, text = p_rectyp)                             # Values acquired from the file disaplyed in table format starting from row 2 column 5
        disL.grid(row = 2, column = 5)

        disp = Label(temp, text = "Facilities")                         # Label text on row 1 column 6
        disp.grid(row = 1, column = 6)
        disL = Label(temp, text = p_recfac)                             # Values acquired from the file disaplyed in table format starting from row 2 column 6
        disL.grid(row = 2, column = 6)

        disp = Label(temp, text = "Capacity")                           # Label text on row 1 column 7
        disp.grid(row = 1, column = 7)
        disL = Label(temp, text = p_reccap)                             # Values acquired from the file disaplyed in table format starting from row 2 column 7
        disL.grid(row = 2, column = 7)

        connect.commit()                                                # Commiting to all the changes made in the file
        connect.close()                                                 # Closing the file {"rooms.db"}

        def closeBF():                                                  # Function to close the window {"temp"} when the button is pressed
            temp.destroy()                                              # Statement to close the {"temp"} window

        closeB = Button(temp, text = 'Exit', command = closeBF)         # The button that invokes the function {"closeBF"} to close the window
        closeB.grid(row = 0, column = 0)

 
    b1top = Button(fr, text = 'By Capacity', command = b1topF)          # Button to invoke the function {"b1topF"} which lets you search by capacity
    b1top.grid(row = 0, column = 0)

    b2top = Button(fr, text = 'By Availability', command = b2topF)      # Button to invoke the function {"b2topF"} which gives data on available rooms
    b2top.grid(row = 0, column = 1)

def onClick1():
    top1 = Tk()                                                         # Creating a window to book the rooms available 
    top1.title('Warwick IT hub - Book')                                 # Assigning the title "Warwick IT hub - Book" to the new window
    connect = sqlite3.connect('rooms.db')                               # Opening the file {"rooms.db"} by connecting it to the variable {"connect"}
    cur = connect.cursor()                                              # Assigning a cursor {"cur"} to browse through the file
    cur.execute('SELECT * FROM rooms')                                  # Query to fetch all the room deatils 
    rec = cur.fetchall()                                                # Fetched values are assigned to {"rec"} variable
    p_recid = ''
    p_recbuild = ''
    p_recname = ''
    p_reccap = ''
    p_rectyp = ''
    p_recfac = '' 
    p_rectim = ''
    p_recbook = ''                                                      # Declaration of variables as NULL values 
    for r in rec:                                                       # Going through all the fetched data
        p_recid += str(r[0]) + '\n'                                     # 'ID' is the First element
        p_recbuild += str(r[1]) + '\n'                                  # 'Building' is the Second element
        p_recname += str(r[2]) + '\n'                                   # 'Name' is the Third element
        p_reccap += str(r[3]) + '\n'                                    # 'Capacity' is the Fourth element
        p_rectyp += str(r[4]) + '\n'                                    # 'Type' is the Fifth element
        p_recfac += str(r[5]) + '\n'                                    # 'Facilities' is the Sixth element
        p_rectim += str(r[6]) + '\n'                                    # 'Time_availability' is the Seventh element
        p_recbook += str(r[7]) + '\n'                                   # 'Booked' is the Eigth element
                                                                        # Assigning the values in the file into the null variables created

    # -------------------- Displaying the values as a table in the GUI window -------------------
    disp = Label(top1, text = "ID")                                     # Label text on row 1 column 1
    disp.grid(row = 1, column = 1)
    disL = Label(top1, text = p_recid)                                  # Values acquired from the file disaplyed in table format starting from row 2 column 1
    disL.grid(row = 2, column = 1)

    disp = Label(top1, text = "Availability")                           # Label text on row 1 column 2
    disp.grid(row = 1, column = 2)
    disL = Label(top1, text = p_rectim)                                 # Values acquired from the file disaplyed in table format starting from row 2 column 2
    disL.grid(row = 2, column = 2)

    disp = Label(top1, text = "Booking")                                # Label text on row 1 column 3
    disp.grid(row = 1, column = 3)
    disL = Label(top1, text = p_recbook)                                # Values acquired from the file disaplyed in table format starting from row 2 column 3
    disL.grid(row = 2, column = 3)

    disp = Label(top1, text = "Building")                               # Label text on row 1 column 4
    disp.grid(row = 1, column = 4)
    disL = Label(top1, text = p_recbuild)                               # Values acquired from the file disaplyed in table format starting from row 2 column 4
    disL.grid(row = 2, column = 4)

    disp = Label(top1, text = "Room Name")                              # Label text on row 1 column 5
    disp.grid(row = 1, column = 5)
    disL = Label(top1, text = p_recname)                                # Values acquired from the file disaplyed in table format starting from row 2 column 5
    disL.grid(row = 2, column = 5)

    disp = Label(top1, text = "Type")                                   # Label text on row 1 column 6
    disp.grid(row = 1, column = 6)
    disL = Label(top1, text = p_rectyp)                                 # Values acquired from the file disaplyed in table format starting from row 2 column 6
    disL.grid(row = 2, column = 6)

    disp = Label(top1, text = "Facilities")                             # Label text on row 1 column 7
    disp.grid(row = 1, column = 7)
    disL = Label(top1, text = p_recfac)                                 # Values acquired from the file disaplyed in table format starting from row 2 column 7
    disL.grid(row = 2, column = 7)

    disp = Label(top1, text = "Capacity")                               # Label text on row 1 column 8
    disp.grid(row = 1, column = 8)
    disL = Label(top1, text = p_reccap)                                 # Values acquired from the file disaplyed in table format starting from row 2 column 8
    disL.grid(row = 2, column = 8)

    connect.commit()                                                    # Commiting to the changes made in the file {"rooms.db"}
    connect.close()                                                     # Closing the file 

    def book():
        v = []                                                          # Initializing an array variable with value NULL
        j = []                                                          # Initializing an array variable with value NULL
        val = int(idcheckE.get())                                       # Storing the value entered as integer into variable {"val"}
        connect = sqlite3.connect('rooms.db')                           # Opening the file {"rooms.db"} by connecting it to the variable {"connect"}
        cur = connect.cursor()                                          # Assigning a cursor {"cur"} to browse through the file

        cur.execute('SELECT id FROM rooms')                             # Query to get the values of element "ID" of each row
        r = cur.fetchall()                                              # Storing the fetched value from the file to variable {"r"}
        for i in r:                                                     # Looping through the elements in {"r"}
            v.append(i[0])                                              # Appending the values fetched from file to variable array {"v"}

        cur.execute('SELECT Booked FROM rooms')                         # Query to get the values of element "Booked" of each row
        k = cur.fetchall()                                              # Storing the fetched values from the file to variable {"k"}
        for i in k:                                                     # Looping through the elements in {"k"}
            j.append(i[0])                                              # Appending the values fetched from file to variable array {"j"}

        m = 0                                                           # Initializing variable {"m"} with value "0"
        for i in v:                                                     # Looping through the values of {"v"} to check the index of the value of {"val"} in the array
            if i == val:                                                
                break                                                   # Breaks if the value is found in the array
            else:
                m += 1                                                  # Each time the value isnt found, the value of {"m"} increments by "1"
        
        if val in v:                                                    # If the value of {"val"} is in the array {"v"}, the following code is executed
            if (j[m] != 'Unavailable'):                                 # If the value in the particular index is "Unavailable", then else statements is executed
                cur.execute('UPDATE rooms SET Booked = "Unavailable" WHERE id =' + str(val))    # Query to update the value of "Booked" to "Unavailable" for the ID that is matching
                messagebox.showinfo('Alert','You have booked the room! Thank you for using the service!')   # If the above query is successful, an alert message pops up saying its successful
                top1.destroy()                                          # Statement to close the window {"top1"}
            else:
                messagebox.showinfo('Alert','The room is already booked \n Enter another ID')   # If the room is "Unavailable", an alert message pops up saying the room is boooked and to enter another ID 
        else:
            messagebox.showinfo('Alert','ID not recognized')            # If the "ID" isn't in the array {"v"}, an alert message pops up saying ID not recognized

        connect.commit()                                                # Commiting the changes made to the file {"rooms.db"}
        connect.close()                                                 # Closing the file 

    fr1 = LabelFrame(top1, padx = 20, pady = 20)                        # A small frame consisting of Label text and a text entry region
    fr1.grid(row = 0, column = 7, columnspan = 2)
    idcheck = Label(fr1, text = 'Enter the ID of the room you want to book: ')  # Label text asking users to enter the ID of the room you want to book
    idcheck.grid(row = 0, column = 0)

    idcheckE = Entry(fr1, text = 'id')                                  # Entry text region where users can enter the ID
    idcheckE.grid(row = 0, column = 1)

    idcheckB = Button(fr1, text = 'Book', command = book)               # Button to book the particular room corresponding to the ID
    idcheckB.grid(row = 0, column = 2)

# --------------------- Starting GUI interface ------------------------
head = Label(frame, text = "Warwick Room Booking")                      # Label saying "Warwick Room Booking"
button = Button(frame, text = "Room Details", command = onClick)        # Button to invoke the function {"onClick"}
button1 = Button(frame, text = "Book Room", command  = onClick1)        # Button to invoke the function {"onClick1"}

head.grid(row = 0, column = 0, columnspan = 2)
button.grid(row = 1, column = 0)
button1.grid(row = 1, column = 1)                                       # Grid layout for the above mentioned labels

root.mainloop()                                                         # This command runs the GUI until the GUI is closed by the user