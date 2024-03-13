#BSIS-NS-3A
#CASTRO, PATRICK JOSUAH
#CORPUZ, MARK JHAY
#DEANG, APRIL JOY
#ESPERO, AIRYSH XANDER

import tkinter as tk
from tkinter import simpledialog, messagebox
import os

def encryptData(data):
    key = 4
    return ''.join(chr(ord(letter) + key) for letter in data)

def decryptData(encryptedData):
    key = 4
    return ''.join(chr(ord(letter) - key) for letter in encryptedData)

def addStudentInfo(student_data):
    with open("Students.txt", "a") as file:
        encrypted_data = [encryptData(data) for data in student_data]
        file.write(','.join(encrypted_data) + '\n')

def displayStudentInfo(studID):
    with open("Students.txt", "r") as file:
        for line in file:
            keyValue = line.strip().split(",")
            if keyValue[0] == studID:
                decrypted_data = [decryptData(data) for data in keyValue]
                messagebox.showinfo("Student Info", 
                                    f"Student ID: {decrypted_data[0]}\n"
                                    f"Student Name: {decrypted_data[1]}, {decrypted_data[2]} {decrypted_data[3]}\n"
                                    f"Section: {decrypted_data[4]}\n"
                                    f"Address: {decrypted_data[5]}")
                break

            else:
                messagebox.showinfo("Error", "Student not found or invalid input.")
                break

root = tk.Tk()
root.title("Student Information System")
root.geometry("600x400")

label_programTitle = tk.Label(root, text="Student Information System", font=("Helvetica", 16))
label_programTitle.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

def showMainWindow():
    root.deiconify()

def popoutWindow():

    def submitData():
        studentId = entry_studentID.get("1.0", "end-1c")
        lastName = entry_lastName.get("1.0", "end-1c")
        firstName = entry_firstName.get("1.0", "end-1c")
        middleName = entry_middleName.get("1.0", "end-1c")
        section = entry_section.get("1.0", "end-1c")
        address = entry_address.get("1.0", "end-1c")
        student_data = [studentId, lastName, firstName, middleName, section, address]
        addStudentInfo(student_data)
        messagebox.showinfo("Success", "Student added successfully!")

        popout_window.destroy()
        showMainWindow()

    root.withdraw()
    popout_window = tk.Toplevel(root)
    popout_window.title("Pop-out Window")
    popout_window.geometry("600x600")

    label_studentID = tk.Label(popout_window, text="Student ID:")
    label_studentID.grid(row=0, column=0, padx=10, pady=10)
    label_studentID.place(relx=0.5, rely=0.075, anchor=tk.CENTER)
    entry_studentID = tk.Text(popout_window, width=30, height=2)
    entry_studentID.grid(row=0, column=1, padx=10, pady=10)
    entry_studentID.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    label_lastName = tk.Label(popout_window, text="Last Name:")
    label_lastName.grid(row=1, column=0, padx=10, pady=10)
    label_lastName.place(relx=0.5, rely=0.225, anchor=tk.CENTER)
    entry_lastName = tk.Text(popout_window, width=30, height=2)
    entry_lastName.grid(row=1, column=1, padx=10, pady=10)
    entry_lastName.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    label_firstName = tk.Label(popout_window, text="First Name:")
    label_firstName.grid(row=2, column=0, padx=10, pady=10)
    label_firstName.place(relx=0.5, rely=0.375, anchor=tk.CENTER)
    entry_firstName = tk.Text(popout_window, width=30, height=2)
    entry_firstName.grid(row=2, column=1, padx=10, pady=10)
    entry_firstName.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

    label_middleName = tk.Label(popout_window, text="Middle Name:")
    label_middleName.grid(row=3, column=0, padx=10, pady=10)
    label_middleName.place(relx=0.5, rely=0.525, anchor=tk.CENTER)
    entry_middleName = tk.Text(popout_window, width=30, height=2)
    entry_middleName.grid(row=3, column=1, padx=10, pady=10)
    entry_middleName.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    label_section = tk.Label(popout_window, text="Section:")
    label_section.grid(row=4, column=0, padx=10, pady=10)
    label_section.place(relx=0.5, rely=0.675, anchor=tk.CENTER)
    entry_section = tk.Text(popout_window, width=30, height=2)
    entry_section.grid(row=4, column=1, padx=10, pady=10)
    entry_section.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    label_address = tk.Label(popout_window, text="Address:")
    label_address.grid(row=5, column=0, padx=10, pady=10)
    label_address.place(relx=0.5, rely=0.825, anchor=tk.CENTER)
    entry_address = tk.Text(popout_window, width=30, height=2)
    entry_address.grid(row=5, column=1, padx=10, pady=10)
    entry_address.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    submit_button = tk.Button(popout_window, text="Submit", command=submitData, width=20, height=2)
    submit_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)
    submit_button.place(relx=0.5, rely=0.975, anchor=tk.CENTER)

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

# New Codes

def searchStudentID(studentID):
    with open("Students.txt", "r") as file:
        for line in file:
            keyValue = line.strip().split(",")
            if keyValue[0] == encryptData(studentID):
                return True
        return False

def updateStudentData():
    studentID = str(input("Enter the student ID: "))
    
    if searchStudentID(studentID):
        print("Please select the data that you want to modify:")
        print("\t 1. Student ID")
        print("\t 2. Last Name")
        print("\t 3. First Name")
        print("\t 4. Middle Name")
        print("\t 5. Section")
        print("\t 6. Address")
        print()
        choice = int(input("Select the number of your choice: "))
        match (choice):
            case 1:
                newStudentID = str(input("Please input the new student ID: "))
                with open("Students.txt", "r") as file:
                    lines = file.readlines()
                if lines:
                    for i, line in enumerate(lines):           
                        data = line.strip().split(',')
                        if data[0] == encryptData(studentID):
                            data[0] = encryptData(newStudentID)
                            newData = data[0]
                            lines[i] = ','.join([newData] + data[1:])  + '\n'
                            with open("Students.txt", "w+") as file:
                                file.writelines(lines)
                            break
            case 2:
                newStudentLastName = str(input("Please input the new student last name: "))
                with open("Students.txt", "r") as file:
                    lines = file.readlines()
                if lines:
                    for i, line in enumerate(lines):
                        data = line.strip().split(',')
                        if data[0] == encryptData(studentID):
                            data[1] = encryptData(newStudentLastName)
                            lines[i] = ','.join(data) + '\n'
                            with open("Students.txt", "w+") as file:
                                file.writelines(lines)
                            break
            case 3:
                newStudentFirstName = str(input("Please input the new student first name: "))
                with open("Students.txt", "r") as file:
                    lines = file.readlines()
                if lines:
                    for i, line in enumerate(lines):
                        data = line.strip().split(',')
                        if data[0] == encryptData(studentID):
                            data[2] = encryptData(newStudentFirstName)
                            lines[i] = ','.join(data) + '\n'
                            with open("Students.txt", "w+") as file:
                                file.writelines(lines)
                            break
            case 4:
                newStudentMiddleName = str(input("Please input the new student middle name: "))
                with open("Students.txt", "r") as file:
                    lines = file.readlines()
                if lines:
                    for i, line in enumerate(lines):
                        data = line.strip().split(',')
                        if data[0] == encryptData(studentID):
                            data[3] = encryptData(newStudentMiddleName)
                            lines[i] = ','.join(data) + '\n'
                            with open("Students.txt", "w+") as file:
                                file.writelines(lines)
                            break
            case 5:
                newStudentSection = str(input("Please input the new student section: "))
                with open("Students.txt", "r") as file:
                    lines = file.readlines()
                if lines:
                    for i, line in enumerate(lines):
                        data = line.strip().split(',')
                        if data[0] == encryptData(studentID):
                            data[4] = encryptData(newStudentSection)
                            lines[i] = ','.join(data) + '\n'
                            with open("Students.txt", "w+") as file:
                                file.writelines(lines)
                            break
            case 6:
                newStudentAddress = str(input("Please input the new student address: "))
                with open("Students.txt", "r") as file:
                    lines = file.readlines()
                if lines:
                    for i, line in enumerate(lines):
                        data = line.strip().split(',')
                        if data[0] == encryptData(studentID):
                            data[5] = encryptData(newStudentAddress)
                            lines[i] = ','.join(data) + '\n'
                            with open("Students.txt", "w+") as file:
                                file.writelines(lines)
                            break
            case _:
                print("Error!")
    else:
        print("The student ID does not exist in the records!")

button_editData = tk.Button(root, text="Update Student Data", command=updateStudentData, width=20, height=2)
button_editData.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

def exit():
    root.destroy()

button_exit = tk.Button(root, text="Exit", command=exit, width=20, height=2)
button_exit.place(relx=0.5, rely=0.80, anchor=tk.CENTER)

root.mainloop()
