from tkinter import *
from PIL import Image,ImageTk
import sqlite3

root = Tk()
root.title("DataBase operations")
root.geometry("400x600")

# Create table
'''
c.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )""") '''

# Create a function to UPDATE a record
def update():
    # Create Database or Connect to one
    conn = sqlite3.connect('address_book.db')
    # Create Curser
    c = conn.cursor()

    record_id = del_box.get()
    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        
        WHERE oid =:oid""",
              {
                  'first': first_name_editor.get(),
                  'last' : last_name_editor.get(),
                  'address': address_editor.get(),
                  'city': city_editor.get(),
                  'state' : state_editor.get(),
                  'zipcode': zip_code_editor.get(),

                  'oid': record_id
              })

    # commit Changes
    conn.commit()
    # Close DataBase
    conn.close()

    # clear the text boxes
    first_name_editor.delete(0,END)
    last_name_editor.delete(0, END)
    address_editor.delete(0, END)
    city_editor.delete(0, END)
    state_editor.delete(0, END)
    zip_code_editor.delete(0, END)

    editor.destroy()


def edit():
    global editor
    editor = Tk()
    editor.title("Update a record")
    editor.geometry("400x300")

    # Create Database or Connect to one
    conn = sqlite3.connect('address_book.db')

    # Create Curser
    c = conn.cursor()

    record_id = del_box.get()
    # Query the database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()

    # Create Global Variable
    global first_name_editor
    global last_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zip_code_editor

    # Create text Boxex
    first_name_editor = Entry(editor, width=30)
    first_name_editor.grid(row=0, column=1, padx=20, pady=5)
    last_name_editor = Entry(editor, width=30)
    last_name_editor.grid(row=1, column=1, padx=20, pady=5)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20, pady=5)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20, pady=5)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20, pady=5)
    zip_code_editor = Entry(editor, width=30)
    zip_code_editor.grid(row=5, column=1, padx=20, pady=5)

    # Create Text Boxes Labels
    first_n_label_editor = Label(editor, text="First Name")
    first_n_label_editor.grid(row=0, column=0)
    last_n_label_editor = Label(editor, text="Last Name")
    last_n_label_editor.grid(row=1, column=0)
    address_label_editor = Label(editor, text="Address")
    address_label_editor.grid(row=2, column=0)
    city_label_editor = Label(editor, text="City")
    city_label_editor.grid(row=3, column=0)
    state_label_editor = Label(editor, text="State")
    state_label_editor.grid(row=4, column=0)
    zip_code_label_editor = Label(editor, text="Zip Code")
    zip_code_label_editor.grid(row=5, column=0)

    # Loop through results
    for record in records:
        first_name_editor.insert(0,record[0])
        last_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zip_code_editor.insert(0, record[5])

    # Create a btn to Save an UPDATED record
    save_btn = Button(editor, text="Update Record", command=update)
    save_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=145)


# Create a function to delete a record
def delete():
    # Create Database or Connect to one
    conn = sqlite3.connect('address_book.db')
    # Create Curser
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from addresses WHERE oid= " + del_box.get())
    del_box.delete(0,END)

    # commit Changes
    conn.commit()
    # Close DataBase
    conn.close()


# Create Submit Function for database
def submit():
    # Create Database or Connect to one
    conn = sqlite3.connect('address_book.db')
    # Create Curser
    c = conn.cursor()

    # Insert values into database
    c.execute("INSERT INTO addresses VALUES (:first_name,:last_name,:address,:city,:state,:zip_code)",
              {'first_name': first_name.get(),
               'last_name': last_name.get(),
               'address': address.get(),
               'city': city.get(),
               'state': state.get(),
               'zip_code': zip_code.get()
                })

    # commit Changes
    conn.commit()
    # Close DataBase
    conn.close()

    # clear the text boxes
    first_name.delete(0,END)
    last_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zip_code.delete(0, END)


# Create Query Function to show records
def query():
    # Create Database or Connect to one
    conn = sqlite3.connect('address_book.db')
    # Create Curser
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # print(records)

    # Loop through results
    print_records = ''
    for record in records:
        print_records += str(record[0])+" " + str(record[1])+" " +"\t" + str(record[6]) + "\n"

    query_label = Label(root,text=print_records)
    query_label.grid(row=13,column=0,columnspan=2)

    # commit Changes
    conn.commit()
    # Close DataBase
    conn.close()


# Create text Boxex
first_name = Entry(root,width =30)
first_name.grid(row=0,column=1,padx=20,pady=5)
last_name = Entry(root,width =30)
last_name.grid(row=1,column=1,padx=20,pady=5)
address = Entry(root,width =30)
address.grid(row=2,column=1,padx=20,pady=5)
city = Entry(root,width =30)
city.grid(row=3,column=1,padx=20,pady=5)
state = Entry(root,width =30)
state.grid(row=4,column=1,padx=20,pady=5)
zip_code = Entry(root,width =30)
zip_code.grid(row=5,column=1,padx=20,pady=5)
del_box = Entry(root,width=30)
del_box.grid(row=9,column=1,padx=20,pady=5)

# Create Text Boxes Labels
first_n_label = Label(root,text="First Name")
first_n_label.grid(row=0,column=0)
last_n_label = Label(root,text="Last Name")
last_n_label.grid(row=1,column=0)
address_label = Label(root,text="Address")
address_label.grid(row=2,column=0)
city_label = Label(root,text="City")
city_label.grid(row=3,column=0)
state_label = Label(root,text="State")
state_label.grid(row=4,column=0)
zip_code_label = Label(root,text="Zip Code")
zip_code_label.grid(row=5,column=0)
update_label = Label(root,text="Select ID")
update_label.grid(row=9,column=0,pady=5)

# Create Button to Add record to the database
my_btn = Button(root,text="SUBMIT",command=submit)
my_btn.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=100)
# Create Query button
query_btn = Button(root,text="Show Records",command=query)
query_btn.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=137)
# Create a btn to DELETE a record
del_btn = Button(root,text="Delete Record", command=delete)
del_btn.grid(row=10,column=0,columnspan=2,padx=10,pady=10,ipadx=136)
# Create a btn to UPDATE a record
update_btn = Button(root,text="Update Record",command=edit)
update_btn.grid(row=11,column=0,columnspan=2,padx=10,pady=10,ipadx=136)

root.mainloop()