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

    def submitData(studentId, lastName, firstName, middleName, section, address):
        student_data = [studentId, lastName, firstName, middleName, section, address]
        addStudentInfo(student_data)
        messagebox.showinfo("Success", "Student added successfully!")

        popout_window.destroy()
        showMainWindow()

    def checkInformations():
        studentId = entry_studentID.get("1.0", "end-1c")
        lastName = entry_lastName.get("1.0", "end-1c")
        firstName = entry_firstName.get("1.0", "end-1c")
        middleName = entry_middleName.get("1.0", "end-1c")
        section = entry_section.get("1.0", "end-1c")
        address = entry_address.get("1.0", "end-1c")
        
        if not studentId or not lastName or not firstName or not middleName or not section or not address: 
            messagebox.showerror("Error", "Please fill out all of the necessary informations!")
        else:
            # studentId = entry_studentID.get().strip()
            with open("Students.txt", "r") as file:
                for line in file:
                    data = line.strip().split(',')
                    if encryptData(studentId) == data[0]:
                        messagebox.showerror("Error", "Student ID already exists!")
                        return False
                    elif encryptData(lastName) == data[1] and encryptData(firstName) == data[2] and encryptData(middleName) == data[3]:
                        messagebox.showerror("Error", "The name of the student already exist under other student ID!")
                        return False
            submitData(studentId, lastName, firstName, middleName, section, address)


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

    submit_button = tk.Button(popout_window, text="Submit", command=checkInformations, width=20, height=2)
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

def search():
    root.withdraw()
    popout_window3 = tk.Toplevel(root)
    popout_window3.title("Search Student")
    popout_window3.geometry("600x350")

    student_id_label = tk.Label(popout_window3, text="Enter the student ID", font=("Helvetica", 12), width=40)
    student_id_label.place(relx=0.5, rely=0.20, anchor=tk.CENTER)

    student_id_entry = tk.Entry(popout_window3, width=40)
    student_id_entry.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

    def backButton():
        popout_window3.destroy()
        showMainWindow()

    def perform_search():
        studentID = student_id_entry.get()
        if not studentID:
            messagebox.showerror("Error", "Please enter the student ID.")
            return
        found = searchStudentID(studentID)
        if found:
            messagebox.showinfo("Found", "Student ID found in the records.")
            popout_window3.destroy()

            def backButton():
                popout_window1.destroy()
                showMainWindow()

            def updateStudentID():
                def submit_update():
                    new_student_id = entry_new_student_id.get().strip()
                    if not new_student_id:
                        messagebox.showerror("Error", "Please enter the new student ID.")
                        return
                    with open("Students.txt", "r") as file:
                        lines = file.readlines()
                        file.seek(0)
                        for i, line in enumerate(lines):
                            data = line.strip().split(',')
                            if data[0] == encryptData(studentID):
                                data[0] = encryptData(new_student_id)
                                lines[i] = ','.join(data) + '\n'
                                with open("Students.txt", "w+") as file:
                                    file.writelines(lines)
                                break
                        else:
                            messagebox.showerror("Error", "Student ID not found.")
                            return
                        messagebox.showinfo("Success", "Student ID updated successfully.")
                        popout_window.destroy()

                popout_window = tk.Toplevel(root)
                popout_window.title("Update Student ID")
                popout_window.geometry("400x200")

                label_new_student_id = tk.Label(popout_window, text="Enter the new student ID:", font=("Helvetica", 12))
                label_new_student_id.grid(row=2, column=0, padx=10, pady=10)

                entry_new_student_id = tk.Entry(popout_window, width=30)
                entry_new_student_id.grid(pady=5)

                button_submit_update = tk.Button(popout_window, text="Submit", command=submit_update)
                button_submit_update.grid(pady=10)


            def updateStudentLN():

                def submit_update():
                    new_student_LN = entry_new_last_name.get().strip()
                    if not new_student_LN:
                        messagebox.showerror("Error", "Please enter the new Last Name.")
                        return
                    with open("Students.txt", "r") as file:
                        lines = file.readlines()
                        file.seek(0)
                        for i, line in enumerate(lines):
                            data = line.strip().split(',')
                            if data[0] == encryptData(studentID):
                                data[1] = encryptData(new_student_LN)
                                lines[i] = ','.join(data) + '\n'
                                with open("Students.txt", "w+") as file:
                                    file.writelines(lines)
                                break
                        else:
                            messagebox.showerror("Error", "Last Name not found.")
                            return
                        messagebox.showinfo("Success", "Last Name updated successfully.")
                        popout_window.destroy()

                popout_window = tk.Toplevel(root)
                popout_window.title("Update Last Name")
                popout_window.geometry("400x200")

                label_new_student_LN = tk.Label(popout_window, text="Enter the new Last Name:", font=("Helvetica", 12))
                label_new_student_LN.pack(pady=10)

                entry_new_last_name = tk.Entry(popout_window, width=30)
                entry_new_last_name.pack(pady=5)

                button_submit_update = tk.Button(popout_window, text="Submit", command=submit_update)
                button_submit_update.pack(pady=10)
            

            def updateStudentFN():

                def submit_update():
                    new_student_FN = entry_new_first_name.get()
                    if not new_student_FN:
                        messagebox.showerror("Error", "Please enter the new First Name.")
                        return
                    with open("Students.txt", "r") as file:
                        lines = file.readlines()
                        file.seek(0)
                        for i, line in enumerate(lines):
                            data = line.strip().split(',')
                            if data[0] == encryptData(studentID):
                                data[2] = encryptData(new_student_FN)
                                lines[i] = ','.join(data) + '\n'
                                with open("Students.txt", "w+") as file:
                                    file.writelines(lines)
                                break
                        else:
                            messagebox.showerror("Error", "First Name not found.")
                            return
                        messagebox.showinfo("Success", "First Name updated successfully.")
                        popout_window.destroy()

                popout_window = tk.Toplevel(root)
                popout_window.title("Update First Name")
                popout_window.geometry("400x200")

                label_new_student_FN = tk.Label(popout_window, text="Enter the new First Name:", font=("Helvetica", 12))
                label_new_student_FN.pack(pady=10)

                entry_new_first_name = tk.Entry(popout_window, width=30)
                entry_new_first_name.pack(pady=5)

                button_submit_update = tk.Button(popout_window, text="Submit", command=submit_update)
                button_submit_update.pack(pady=10)

            def updateStudentMN():

                def submit_update():
                    new_student_MN = entry_new_middle_name.get()
                    if not new_student_MN:
                        messagebox.showerror("Error", "Please enter the new Middle Name.")
                        return
                    with open("Students.txt", "r") as file:
                        lines = file.readlines()
                        file.seek(0)
                        for i, line in enumerate(lines):
                            data = line.strip().split(',')
                            if data[0] == encryptData(studentID):
                                data[3] = encryptData(new_student_MN)
                                lines[i] = ','.join(data) + '\n'
                                with open("Students.txt", "w+") as file:
                                    file.writelines(lines)
                                break
                        else:
                            messagebox.showerror("Error", "Middle Name not found.")
                            return
                        messagebox.showinfo("Success", "Middle Name updated successfully.")
                        popout_window.destroy()

                popout_window = tk.Toplevel(root)
                popout_window.title("Update Middle Name")
                popout_window.geometry("400x200")

                label_new_student_MN = tk.Label(popout_window, text="Enter the new Middle Name:", font=("Helvetica", 12))
                label_new_student_MN.pack(pady=10)

                entry_new_middle_name = tk.Entry(popout_window, width=30)
                entry_new_middle_name.pack(pady=5)

                button_submit_update = tk.Button(popout_window, text="Submit", command=submit_update)
                button_submit_update.pack(pady=10)

            def updateStudentSection():

                def submit_update():
                    new_student_sec = entry_new_section.get().strip()
                    if not new_student_sec:
                        messagebox.showerror("Error", "Please enter the new Section.")
                        return
                    with open("Students.txt", "r") as file:
                        lines = file.readlines()
                        file.seek(0)
                        for i, line in enumerate(lines):
                            data = line.strip().split(',')
                            if data[0] == encryptData(studentID):
                                data[4] = encryptData(new_student_sec)
                                lines[i] = ','.join(data) + '\n'
                                with open("Students.txt", "w+") as file:
                                    file.writelines(lines)
                                break
                        else:
                            messagebox.showerror("Error", "Section not found.")
                            return
                        messagebox.showinfo("Success", "Section updated successfully.")
                        popout_window.destroy()

                popout_window = tk.Toplevel(root)
                popout_window.title("Update Section")
                popout_window.geometry("400x200")

                label_new_student_sec = tk.Label(popout_window, text="Enter the new Section:", font=("Helvetica", 12))
                label_new_student_sec.pack(pady=10)

                entry_new_section = tk.Entry(popout_window, width=30)
                entry_new_section.pack(pady=5)

                button_submit_update = tk.Button(popout_window, text="Submit", command=submit_update)
                button_submit_update.pack(pady=10)

            def updateStudentAddress():

                def submit_update():
                    new_student_adrs = entry_new_address.get()
                    if not new_student_adrs:
                        messagebox.showerror("Error", "Please enter the new Address.")
                        return
                    with open("Students.txt", "r") as file:
                        lines = file.readlines()
                        file.seek(0)
                        for i, line in enumerate(lines):
                            data = line.strip().split(',')
                            if data[0] == encryptData(studentID):
                                data[5] = encryptData(new_student_adrs)
                                lines[i] = ','.join(data) + '\n'
                                with open("Students.txt", "w+") as file:
                                    file.writelines(lines)
                                break
                        else:
                            messagebox.showerror("Error", "Address not found.")
                            return
                        messagebox.showinfo("Success", "Address updated successfully.")
                        popout_window.destroy()

                popout_window = tk.Toplevel(root)
                popout_window.title("Update Address")
                popout_window.geometry("400x200")

                label_new_student_adrs = tk.Label(popout_window, text="Enter the new Address:", font=("Helvetica", 12))
                label_new_student_adrs.pack(pady=10)

                entry_new_address = tk.Entry(popout_window, width=30)
                entry_new_address.pack(pady=5)

                button_submit_update = tk.Button(popout_window, text="Submit", command=submit_update)
                button_submit_update.pack(pady=10)

            root.withdraw()
            popout_window1 = tk.Toplevel(root)
            popout_window1.title("Pop-out Window1")
            popout_window1.geometry("600x500")

            label_programTitle2 = tk.Label(popout_window1, text="Update Student Information Records", font=("Helvetica", 16))
            label_programTitle2.place(relx=0.5, rely=0.10, anchor=tk.CENTER)

            button_updateStudentID = tk.Button(popout_window1, text="Update Student ID", command=updateStudentID, width=40, height=2)
            button_updateStudentID.place(relx=0.5, rely=0.20, anchor=tk.CENTER)

            button_updateStudentLastName = tk.Button(popout_window1, text="Update Student Last Name", command=updateStudentLN, width=40, height=2)
            button_updateStudentLastName.place(relx=0.5, rely=0.32, anchor=tk.CENTER)

            button_updateStudentFirstName = tk.Button(popout_window1, text="Update Student First Name", command=updateStudentFN, width=40, height=2)
            button_updateStudentFirstName.place(relx=0.5, rely=0.44, anchor=tk.CENTER)

            button_updateStudentMiddleName = tk.Button(popout_window1, text="Update Student Middle Name", command=updateStudentMN, width=40, height=2)
            button_updateStudentMiddleName.place(relx=0.5, rely=0.56, anchor=tk.CENTER)

            button_updateStudentSection = tk.Button(popout_window1, text="Update Student Section", command=updateStudentSection, width=40, height=2)
            button_updateStudentSection.place(relx=0.5, rely=0.68, anchor=tk.CENTER)

            button_updateStudentAddress = tk.Button(popout_window1, text="Update Student Address", command=updateStudentAddress, width=40, height=2)
            button_updateStudentAddress.place(relx=0.5, rely=0.80, anchor=tk.CENTER)

            button_backButton = tk.Button(popout_window1, text="Back", command=backButton, width=40, height=2)
            button_backButton.place(relx=0.5, rely=0.92, anchor=tk.CENTER)
        else:
            messagebox.showinfo("Not Found", "Student ID not found in the records.")

    search_button = tk.Button(popout_window3, text="Search", command=perform_search, width=20, height=2)
    search_button.place(relx=0.5, rely=0.50, anchor=tk.CENTER)

    back_button = tk.Button(popout_window3, text="Back", command=backButton, width=20, height=2)
    back_button.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

    popout_window3.mainloop()

button_editData = tk.Button(root, text="Update Student Data", command=search, width=20, height=2)
button_editData.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

def exit():
    root.destroy()

button_exit = tk.Button(root, text="Exit", command=exit, width=20, height=2)
button_exit.place(relx=0.5, rely=0.80, anchor=tk.CENTER)

root.mainloop()