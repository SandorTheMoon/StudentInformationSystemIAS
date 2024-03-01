# Group Members:
# Castro, Patrick Josuah B.
# Corpuz, Mark Jhay
# Deang, April Joy L.
# Espero, Airysh Xander M.


import tkinter as tk
from tkinter import simpledialog, messagebox
import os

def encryptData(data):
    key = 4
    return ''.join(chr(ord(letter) + key) for letter in data)

def decryptData(encryptedData):
    key = 4
    return ''.join(chr(ord(letter) - key) for letter in encryptedData)

def displayStudentInfo(studID):
    found = False
    with open("Students.txt", "r") as file:
        for line in file:
            keyValue = line.strip().split(",")
            if keyValue[0] == studID:
                decrypted_data = [decryptData(data) for data in keyValue]
                found = True
                messagebox.showinfo("Student Info", 
                                    f"Student ID: {decrypted_data[0]}\n"
                                    f"Student Name: {decrypted_data[1]}, {decrypted_data[2]} {decrypted_data[3]}\n"
                                    f"Section: {decrypted_data[4]}\n"
                                    f"Address: {decrypted_data[5]}")
                break
    
    if not found:
        messagebox.showinfo("Error", "Student not found or invalid input.")


root = tk.Tk()
root.title("Student Information System")
root.geometry("600x400")

label_programTitle = tk.Label(root, text="Student Information System", font=("Helvetica", 16))
label_programTitle.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

def showMainWindow():
    root.deiconify()

def popoutWindow():

    def closeCurrentWindow():
        popout_window.destroy()
        showMainWindow()

    root.withdraw()
    popout_window = tk.Toplevel(root)
    popout_window.title("Pop-out Window")
    popout_window.geometry("600x400")

    label_studentID = tk.Label(popout_window, text="Student ID:")
    label_studentID.grid(row=0, column=0, padx=10, pady=10)
    label_studentID.place(relx=0.5, rely=0.075, anchor=tk.CENTER)
    entry = tk.Text(popout_window, width=30, height=2)
    entry.grid(row=0, column=1, padx=10, pady=10)
    entry.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    label_firstName = tk.Label(popout_window, text="First Name:")
    label_firstName.grid(row=1, column=0, padx=10, pady=10)
    label_firstName.place(relx=0.5, rely=0.225, anchor=tk.CENTER)
    entry = tk.Text(popout_window, width=30, height=2)
    entry.grid(row=1, column=1, padx=10, pady=10)
    entry.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    label_middleName = tk.Label(popout_window, text="Middle Name:")
    label_middleName.grid(row=2, column=0, padx=10, pady=10)
    label_middleName.place(relx=0.5, rely=0.375, anchor=tk.CENTER)
    entry = tk.Text(popout_window, width=30, height=2)
    entry.grid(row=2, column=1, padx=10, pady=10)
    entry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

    label_section = tk.Label(popout_window, text="Section:")
    label_section.grid(row=3, column=0, padx=10, pady=10)
    label_section.place(relx=0.5, rely=0.525, anchor=tk.CENTER)
    entry = tk.Text(popout_window, width=30, height=2)
    entry.grid(row=3, column=1, padx=10, pady=10)
    entry.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    label_address = tk.Label(popout_window, text="Address:")
    label_address.grid(row=4, column=0, padx=10, pady=10)
    label_address.place(relx=0.5, rely=0.675, anchor=tk.CENTER)
    entry = tk.Text(popout_window, width=30, height=2)
    entry.grid(row=4, column=1, padx=10, pady=10)
    entry.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    submit_button = tk.Button(popout_window, text="Submit", command=closeCurrentWindow, width=20, height=2)
    submit_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
    submit_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def getStudentID():
    root = tk.Tk()
    root.withdraw()
    student_id = simpledialog.askstring("Student ID", "Enter Student ID (e.g TUPM-20-1234): ")
    if student_id:
        root.destroy()
        displayStudentInfo(encryptData(student_id))
    else:
        root.destroy()
        messagebox.showinfo("Error", "Invalid Student ID!")
        root.mainloop()

button_inputData = tk.Button(root, text="Input Data", command=popoutWindow, width=20, height=2)
button_inputData.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

button_viewData= tk.Button(root, text="View Data", command=getStudentID, width=20, height=2)
button_viewData.place(relx=0.5, rely=0.50, anchor=tk.CENTER)

def exit():
    root.destroy()

button_viewData= tk.Button(root, text="Exit", command=exit, width=20, height=2)
button_viewData.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

root.mainloop()

#--- CODE DATI: ---

# import os

# def stringToArray(iD, lName, fName, mName, sect, addr):
#     arrayID = [char for char in iD]
#     arrayLastName = [char for char in lName]
#     arrayFirstName = [char for char in fName]
#     arrayMiddleName = [char for char in mName]
#     arraySection = [char for char in sect]
#     arrayAddress = [char for char in addr]

#     encryptData(arrayID, arrayLastName, arrayFirstName, arrayMiddleName, arraySection, arrayAddress)

# def encryptData(iD, lName, fName, mName, sect, addr):
#     key = 4

#     encryptId = ''.join([chr((ord(letter) + key)) for letter in iD])
#     encryptLastName = ''.join([chr((ord(letter) + key)) for letter in lName])
#     encryptFirstName = ''.join([chr((ord(letter) + key)) for letter in fName])
#     encryptMiddleName = ''.join([chr((ord(letter) + key)) for letter in mName])
#     encryptSection = ''.join([chr((ord(letter) + key)) for letter in sect])
#     encryptAddress = ''.join([chr((ord(letter) + key)) for letter in addr])

#     addStudentInfo(encryptId, encryptLastName, encryptFirstName, encryptMiddleName, encryptSection, encryptAddress)

# def decryptData(encryptedData):
#     key = 4
#     decrypted_data = ""

#     for letter in encryptedData:
#         decrypted_data += chr((ord(letter) - key))

#     return decrypted_data

# def addStudentInfo(iD, lName, fName, mName, sect, addr):
#     with open("Students.txt", "a") as file:
#         file.write(f"{iD},{lName},{fName},{mName},{sect},{addr}\n")

# def displayStudentInfo(studID):
#     with open("Students.txt", "r") as file:
#         for line in file:
#             keyValue = line.strip().split(",")

#             if keyValue[0] == str(studID):
#                 studentIdDecrypted = decryptData(keyValue[0])
#                 studentLastNameDecrypted = decryptData(keyValue[1])
#                 studentFirstNameDecrypted = decryptData(keyValue[2])
#                 studentMiddleNameDecrypted = decryptData(keyValue[3])
#                 studentSectionDecrypted = decryptData(keyValue[4])
#                 studentAddressDecrypted = decryptData(keyValue[5])

#                 os.system("cls")
#                 print("--- Student Info ---")
#                 print(f"Student ID: {studentIdDecrypted}")
#                 print(f"Name: {studentLastNameDecrypted}, {studentFirstNameDecrypted} {studentMiddleNameDecrypted}")
#                 print(f"Section: {studentSectionDecrypted}")
#                 print(f"Address: {studentAddressDecrypted}")

#             else:
#                 os.system("cls")
#                 print("Student not found or invalid input.")

#         os.system("pause")
        

# while True:
#     try:
#         os.system("cls")
#         print("--- Student Information System ---")
#         print("1. Input Data")
#         print("2. View Data")
#         choice = int(input("Choose option: "))

#         if (choice == 1):
#             os.system("cls")
#             print("--- Add Student Information ---")
#             studentId = str(input("Student ID: "))
#             lastName = str(input("Last Name: "))
#             firstName = str(input("First Name: "))
#             midName = str(input("Middle Name: "))
#             section = str(input("Section: "))
#             address = str(input("Address: "))
#             stringToArray(studentId, lastName, firstName, midName, section, address)
#             print("Student added...")
#             os.system("pause")

#         elif (choice == 2):
#             os.system("cls")
#             print("--- Find Student Information ---")
#             getStudentId = str(input("Enter Student ID (e.g TUPM-20-1234): "))
#             getStudentIdArray = [char for char in getStudentId]
#             getStudentIdEncrypted = ""

#             for letter in getStudentIdArray:
#                 key = 4
#                 getStudentIdEncrypted += chr((ord(letter) + key))

#             displayStudentInfo(getStudentIdEncrypted)

#         else:
#             os.system("cls")
#             print("Invalid option!")
#             os.system("pause")
    
#     except ValueError:
#         os.system("cls")
#         print("Invalid input!")
#         os.system("pause")
