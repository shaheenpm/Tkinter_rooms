from tkinter import *
import sqlite3                                                          # Imports the SQL statements

root = Tk()                                                             # Window Created
root.title("Create Database")

# ---------------------------- Function definitions --------------------------------
def submitN():
    connect = sqlite3.connect('rooms.db')                               # {"rooms.db"} file opened with the use of {"connect"} variable
    cur = connect.cursor()                                              # Cursor {"cur"} is assigned to browse through the file
    cur.execute('INSERT INTO rooms VALUES (:id_no, :build, :name, :capacity, :type_t, :fac, :tim, :book)',
        {
            'id_no': id_no.get(),                                       # "get()" is used to get the value entered in the text area
            'build': build.get(),                                       # All the entries are added to the file {"rooms.db"} through the get()
            'name': name.get(),
            'capacity': capacity.get(),
            'type_t': type_t.get(),
            'fac': fac.get(),
            'tim': tim.get(),
            'book': book.get()
        })                                                              # Query to add elements into the dataset {"rooms.db"}
    connect.commit()                                                    # Commiting the changes made in the file
    connect.close()                                                     # Closing the file
    id_no.delete(0, END)                                                # When the entries are submitted, the text area is cleared using this command
    build.delete(0, END)
    name.delete(0, END)
    capacity.delete(0, END)
    type_t.delete(0, END)
    fac.delete(0, END)
    tim.delete(0, END)
    book.delete(0, END)

# -------------------------- Function to display the contents in file -------------------------------
def displayC():
    connect = sqlite3.connect('rooms.db')                               # Variable {"connect"} used to open the file {"rooms.db"}
    cur = connect.cursor()                                              # Cursor {"cur"} used to browse through the contents 
    cur.execute('SELECT *, oid FROM rooms')                             # Query used to fetch all the details in the file {"rooms.db"}
    rec = cur.fetchall()                                                # Fetched results are stored into the variable {"rec"}

    p_recid = ''
    p_recbuild = ''
    p_recname = ''
    p_reccap = ''
    p_rectyp = ''
    p_recfac = '' 
    p_rectim = ''
    p_recbook = ''                                                      # Variables initialized with a NULL value
    for r in rec:                                                       # Looping through the {"rec"} variable
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
    disp = Label(root, text = "ID")                                     # Label text on row 11 column 0
    disp.grid(row = 11, column = 0)
    disL = Label(root, text = p_recid)                                  # Values acquired from the file disaplyed in table format starting from row 12 column 0
    disL.grid(row = 12, column = 0)

    disp = Label(root, text = "Building")                               # Label text on row 11 column 1
    disp.grid(row = 11, column = 1)
    disL = Label(root, text = p_recbuild)                               # Values acquired from the file disaplyed in table format starting from row 12 column 1
    disL.grid(row = 12, column = 1)

    disp = Label(root, text = "Room Name")                              # Label text on row 11 column 2
    disp.grid(row = 11, column = 2)
    disL = Label(root, text = p_recname)                                # Values acquired from the file disaplyed in table format starting from row 12 column 2
    disL.grid(row = 12, column = 2)

    disp = Label(root, text = "Capacity")                               # Label text on row 11 column 3
    disp.grid(row = 11, column = 3)
    disL = Label(root, text = p_reccap)                                 # Values acquired from the file disaplyed in table format starting from row 12 column 3
    disL.grid(row = 12, column = 3)

    disp = Label(root, text = "Type")                                   # Label text on row 11 column 4
    disp.grid(row = 11, column = 4)
    disL = Label(root, text = p_rectyp)                                 # Values acquired from the file disaplyed in table format starting from row 12 column 4
    disL.grid(row = 12, column = 4)

    disp = Label(root, text = "Facilities")                             # Label text on row 11 column 5
    disp.grid(row = 11, column = 5)
    disL = Label(root, text = p_recfac)                                 # Values acquired from the file disaplyed in table format starting from row 12 column 5
    disL.grid(row = 12, column = 5)

    disp = Label(root, text = "Availability")                           # Label text on row 11 column 6
    disp.grid(row = 11, column = 6)
    disL = Label(root, text = p_rectim)                                 # Values acquired from the file disaplyed in table format starting from row 12 column 6
    disL.grid(row = 12, column = 6)

    disp = Label(root, text = "Booking")                                # Label text on row 11 column 7
    disp.grid(row = 11, column = 7)
    disL = Label(root, text = p_recbook)                                # Values acquired from the file disaplyed in table format starting from row 12 column 7
    disL.grid(row = 12, column = 7)

    connect.commit()                                                    # Committing the changes made in the file {"rooms.db"}
    connect.close()                                                     # Closing the file


# -------------------------- The user entry area ------------------------------
id_noL = Label(root, text = "ID: ")                                     # Label for accepting "ID"
id_noL.grid(row = 0, column = 0)
buildL = Label(root, text = "Building: ")                               # Label for accepting "Building"
buildL.grid(row = 1, column = 0)
nameL = Label(root, text = "Name: ")                                    # Label for accepting "Name"
nameL.grid(row = 2, column = 0)
capacityL = Label(root, text = "Capacity: ")                            # Label for accepting "Capacity"
capacityL.grid(row = 3, column = 0)
type_tL = Label(root, text = "Type: ")                                  # Label for accepting "Type"
type_tL.grid(row = 4, column = 0)
facL = Label(root, text = "Facilities: ")                               # Label for accepting "Facilities"
facL.grid(row = 5, column = 0)
timL = Label(root, text = "Availability: ")                             # Label for accepting "Availability"
timL.grid(row = 6, column = 0)
bookL = Label(root, text = "Booking: ")                                 # Label for accepting "Booking"
bookL.grid(row = 7, column = 0)

id_no = Entry(root, width = 30)                                         # Text Area to enter the value of "ID"
id_no.grid(row = 0, column = 1)
build = Entry(root, width = 30)                                         # Text Area to enter the value of "Building"
build.grid(row = 1, column = 1)
name = Entry(root, width = 30)                                          # Text Area to enter the value of "Name"
name.grid(row = 2, column = 1)
capacity = Entry(root, width = 30)                                      # Text Area to enter the value of "Capacity"
capacity.grid(row = 3, column = 1)
type_t = Entry(root, width = 30)                                        # Text Area to enter the value of "Type"
type_t.grid(row = 4, column = 1)
fac = Entry(root, width = 30)                                           # Text Area to enter the value of "Facilities"
fac.grid(row = 5, column = 1)
tim = Entry(root, width = 30)                                           # Text Area to enter the value of "Availability"
tim.grid(row = 6, column = 1)
book = Entry(root, width = 30)                                          # Text Area to enter the value of "Booking"
book.grid(row = 7, column = 1)

# ----------------------------- Buttons used in the window -------------------------------
submit = Button(root, text = 'Submit', command = submitN)               # Button to submit the values entered and to invoke the function {"submitN"}
submit.grid(row = 8, column = 0, columnspan = 2)

display = Button(root, text = "Display content", command = displayC)    # Button to display the values entered and to invoke the function {"displayC"}
display.grid(row = 9, column = 0, columnspan = 2)

root.mainloop()                                                         # This command lets you run the GUI until the user closes the interface