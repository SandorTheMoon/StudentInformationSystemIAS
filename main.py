#BSIS-NS-3A
#CASTRO, PATRICK JOSUAH
#CORPUZ, MARK JHAY
#DEANG, APRIL JOY
#ESPERO, AIRYSH XANDER

import tkinter as tk
from tkinter import simpledialog, messagebox
import os


#========== OTHER PROGRAM BACKEND FUNCTIONS ==========#
def encryptData(data):
    key = 4
    return ''.join(chr(ord(letter) + key) for letter in data)

def decryptData(encryptedData):
    key = 4
    return ''.join(chr(ord(letter) - key) for letter in encryptedData)

def addStudentInfo(student_data):
    with open(filename, "a") as file:
        encrypted_data = [encryptData(data) for data in student_data]
        file.write(','.join(encrypted_data) + '\n')

def deleteStudentInfo(studID):
    found = False

    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            keyValue = line.strip().split(",")

            if keyValue[0] == encryptData(studID):
                messagebox.showinfo("Success", f"Student ID ({studID}) has been deleted.")
                found = True
                
            else:
                file.write(line)

    if not found:
        messagebox.showinfo("Error", "Student not found or invalid input.")

def displayStudentInfo(studID):
    found = False

    with open(filename, "r") as file:
        for line in file:
            keyValue = line.strip().split(",")

            if keyValue[0] == studID:
                decrypted_data = [decryptData(data) for data in keyValue]
                messagebox.showinfo("Student Info", 
                                    f"Student ID: {decrypted_data[0]}\n"
                                    f"Student Name: {decrypted_data[1]}, {decrypted_data[2]} {decrypted_data[3]}\n"
                                    f"Section: {decrypted_data[4]}\n"
                                    f"Address: {decrypted_data[5]}")
                found = True
                break

        if not found:
            messagebox.showinfo("Error", "Student not found or invalid input.")


#===== File Encryption and Initialization =====#
def encryptFileName():
    file = encryptData("Students")
    return file

filename = encryptFileName() + ".txt"
createFile = open(filename, "w")
createFile.close()


#========== TO SHOW MAIN MENU WINDOW ==========#
def showMainWindow():
    root.deiconify()


#========== WINDOW FOR ADD STUDENT ==========#    
def AddStudent():

    def checkNewStudent():
        studentId = entry_studentID.get("1.0", "end-1c")
        lastName = entry_lastName.get("1.0", "end-1c")
        firstName = entry_firstName.get("1.0", "end-1c")
        middleName = entry_middleName.get("1.0", "end-1c")
        section = entry_section.get("1.0", "end-1c")
        address = entry_address.get("1.0", "end-1c")
        
        if not studentId or not lastName or not firstName or not middleName or not section or not address: 
            messagebox.showerror("Error", "Please fill out all of the necessary informations!")

        else:
            with open(filename, "r") as file:
                for line in file:
                    data = line.strip().split(',')

                    if encryptData(studentId) == data[0]:
                        messagebox.showerror("Error", "Student ID already exists!")
                        return False
                    
                    elif encryptData(lastName) == data[1] and encryptData(firstName) == data[2] and encryptData(middleName) == data[3]:
                        messagebox.showerror("Error", "The name of the student already exist under other student ID!")
                        return False
                    
            student_data = [studentId, lastName, firstName, middleName, section, address]
            addStudentInfo(student_data)
            messagebox.showinfo("Success", "Student added successfully!")

            AddStudent_window.destroy()
            showMainWindow()

    def backButton():
        AddStudent_window.destroy()
        showMainWindow()

    root.withdraw()
    AddStudent_window = tk.Toplevel(root)
    AddStudent_window.title("Pop-out Window")
    AddStudent_window.geometry("600x575")

    label_newStudent = tk.Label(AddStudent_window, text="Add Student", font=("Helvetica", 12))
    label_newStudent.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    label_studentID = tk.Label(AddStudent_window, text="Student ID:")
    label_studentID.place(relx=0.5, rely=0.10, anchor=tk.CENTER)
    entry_studentID = tk.Text(AddStudent_window, width=30, height=2)
    entry_studentID.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    label_lastName = tk.Label(AddStudent_window, text="Last Name:")
    label_lastName.place(relx=0.5, rely=0.20, anchor=tk.CENTER)
    entry_lastName = tk.Text(AddStudent_window, width=30, height=2)
    entry_lastName.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    label_firstName = tk.Label(AddStudent_window, text="First Name:")
    label_firstName.place(relx=0.5, rely=0.30, anchor=tk.CENTER)
    entry_firstName = tk.Text(AddStudent_window, width=30, height=2)
    entry_firstName.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

    label_middleName = tk.Label(AddStudent_window, text="Middle Name:")
    label_middleName.place(relx=0.5, rely=0.40, anchor=tk.CENTER)
    entry_middleName = tk.Text(AddStudent_window, width=30, height=2)
    entry_middleName.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

    label_section = tk.Label(AddStudent_window, text="Section:")
    label_section.place(relx=0.5, rely=0.50, anchor=tk.CENTER)
    entry_section = tk.Text(AddStudent_window, width=30, height=2)
    entry_section.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

    label_address = tk.Label(AddStudent_window, text="Address:")
    label_address.place(relx=0.5, rely=0.60, anchor=tk.CENTER)
    entry_address = tk.Text(AddStudent_window, width=30, height=2)
    entry_address.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

    submit_button = tk.Button(AddStudent_window, text="Submit", command=checkNewStudent, width=20, height=2)
    submit_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    back_button = tk.Button(AddStudent_window, text="Back", command=backButton, width=20, height=2)
    back_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)


#========== WINDOW FOR VIEW STUDENT ==========#
def ViewStudent():
    getStudentId_window = tk.Tk()
    getStudentId_window.withdraw()
    student_id = simpledialog.askstring("Student ID", "Enter Student ID (e.g TUPM-20-1234): ")

    if student_id:
        getStudentId_window.destroy()
        displayStudentInfo(encryptData(student_id))

    else:
        getStudentId_window.destroy()
        messagebox.showinfo("Error", "Invalid Student ID!")
        showMainWindow()


#========== WINDOW FOR UPDATE STUDENT ==========#
def UpdateStudent():

    def backButton1():
        getStudentId_window.destroy()
        showMainWindow()

    def searchStudentID(studentID):
        with open(filename, "r") as file:
            for line in file:
                keyValue = line.strip().split(",")
                
                if keyValue[0] == encryptData(studentID):
                    return True

            return False

    def perform_search():
        studentID = student_id_entry.get("1.0", "end-1c")
        found = searchStudentID(studentID)

        def submit_update(studentData, index):
            with open(filename, "r") as file:
                lines = file.readlines()
                
                for i, line in enumerate(lines):
                    data = line.strip().split(',')

                    if data[0] == encryptData(studentID):
                        data[index] = encryptData(studentData)
                        lines[i] = ','.join(data) + '\n'

                        with open(filename, "w+") as file:
                            file.writelines(lines)
                        break
                
                messagebox.showinfo("Success", "Information updated successfully.")

        if not studentID:
            messagebox.showerror("Error", "Please enter a student ID.")
        
        if found:
            getStudentId_window.destroy()

            def updateStudentID():

                def backButton2():
                    popout_window.destroy()
                    studentNewUpdate_window.deiconify()

                def submitID():
                    new_student_ID = entry_new_student_id.get().strip()
                    index = 0

                    if not new_student_ID:
                        messagebox.showerror("Error", "Please enter a new Student ID.")
                        
                    else:
                        submit_update(new_student_ID, index)
                        popout_window.destroy()
                        studentNewUpdate_window.destroy()
                        showMainWindow()

                popout_window = tk.Toplevel(root)
                popout_window.title("Update Student ID")
                popout_window.geometry("400x350")

                label_new_student_id = tk.Label(popout_window, text="Enter the new student ID:", font=("Helvetica", 12))
                label_new_student_id.place(relx=0.5, rely=0.20, anchor=tk.CENTER)

                entry_new_student_id = tk.Entry(popout_window, width=40)
                entry_new_student_id.place(relx=0.5, rely=0.325, anchor=tk.CENTER)

                button_submit_update = tk.Button(popout_window, text="Submit", command=submitID, width=20, height=2)
                button_submit_update.place(relx=0.5, rely=0.475, anchor=tk.CENTER)

                back_button = tk.Button(popout_window, text="Back", command=backButton2, width=20, height=2)
                back_button.place(relx=0.5, rely=0.625, anchor=tk.CENTER)

            def updateStudentLN():

                def backButton2():
                    popout_window.destroy()
                    studentNewUpdate_window.deiconify()

                def submitLN():
                    new_student_LN = entry_new_last_name.get().strip()
                    index = 1

                    if not new_student_LN:
                        messagebox.showerror("Error", "Please enter a new Last Name.")
                        
                    else:
                        submit_update(new_student_LN, index)
                        popout_window.destroy()

                popout_window = tk.Toplevel(root)
                popout_window.title("Update Last Name")
                popout_window.geometry("400x350")

                label_new_student_LN = tk.Label(popout_window, text="Enter the new Last Name:", font=("Helvetica", 12))
                label_new_student_LN.place(relx=0.5, rely=0.20, anchor=tk.CENTER)

                entry_new_last_name = tk.Entry(popout_window, width=40)
                entry_new_last_name.place(relx=0.5, rely=0.325, anchor=tk.CENTER)

                button_submit_update = tk.Button(popout_window, text="Submit", command=submitLN, width=20, height=2)
                button_submit_update.place(relx=0.5, rely=0.475, anchor=tk.CENTER)

                back_button = tk.Button(popout_window, text="Back", command=backButton2, width=20, height=2)
                back_button.place(relx=0.5, rely=0.625, anchor=tk.CENTER)
            
            def updateStudentFN():
                
                def backButton2():
                    popout_window.destroy()
                    studentNewUpdate_window.deiconify()

                def submitFN():
                    new_student_FN = entry_new_first_name.get().strip()
                    index = 2

                    if not new_student_FN:
                        messagebox.showerror("Error", "Please enter a new First Name.")
                        
                    else:
                        submit_update(new_student_FN, index)
                        popout_window.destroy()

                popout_window = tk.Toplevel(root)
                popout_window.title("Update First Name")
                popout_window.geometry("400x350")

                label_new_student_FN = tk.Label(popout_window, text="Enter the new First Name:", font=("Helvetica", 12))
                label_new_student_FN.place(relx=0.5, rely=0.20, anchor=tk.CENTER)

                entry_new_first_name = tk.Entry(popout_window, width=40)
                entry_new_first_name.place(relx=0.5, rely=0.325, anchor=tk.CENTER)

                button_submit_update = tk.Button(popout_window, text="Submit", command=submitFN, width=20, height=2)
                button_submit_update.place(relx=0.5, rely=0.475, anchor=tk.CENTER)

                back_button = tk.Button(popout_window, text="Back", command=backButton2, width=20, height=2)
                back_button.place(relx=0.5, rely=0.625, anchor=tk.CENTER)
            
            def updateStudentMN():

                def backButton2():
                    popout_window.destroy()
                    studentNewUpdate_window.deiconify()

                def submitMN():
                    new_student_MN = entry_new_middle_name.get().strip()
                    index = 3

                    if not new_student_MN:
                        messagebox.showerror("Error", "Please enter a new Middle Name.")
                        
                    else:
                        submit_update(new_student_MN, index)
                        popout_window.destroy()

                popout_window = tk.Toplevel(root)
                popout_window.title("Update Middle Name")
                popout_window.geometry("400x350")

                label_new_student_MN = tk.Label(popout_window, text="Enter the new Middle Name:", font=("Helvetica", 12))
                label_new_student_MN.place(relx=0.5, rely=0.20, anchor=tk.CENTER)

                entry_new_middle_name = tk.Entry(popout_window, width=40)
                entry_new_middle_name.place(relx=0.5, rely=0.325, anchor=tk.CENTER)

                button_submit_update = tk.Button(popout_window, text="Submit", command=submitMN, width=20, height=2)
                button_submit_update.place(relx=0.5, rely=0.475, anchor=tk.CENTER)

                back_button = tk.Button(popout_window, text="Back", command=backButton2, width=20, height=2)
                back_button.place(relx=0.5, rely=0.625, anchor=tk.CENTER)

            def updateStudentSection():

                def backButton2():
                    popout_window.destroy()
                    studentNewUpdate_window.deiconify()

                def submitSection():
                    new_student_section = entry_new_section.get().strip()
                    index = 4

                    if not new_student_section:
                        messagebox.showerror("Error", "Please enter a new Section.")
                        
                    else:
                        submit_update(new_student_section, index)
                        popout_window.destroy()

                popout_window = tk.Toplevel(root)
                popout_window.title("Update Section")
                popout_window.geometry("400x350")

                label_new_student_sec = tk.Label(popout_window, text="Enter the new Section:", font=("Helvetica", 12))
                label_new_student_sec.place(relx=0.5, rely=0.20, anchor=tk.CENTER)

                entry_new_section = tk.Entry(popout_window, width=40)
                entry_new_section.place(relx=0.5, rely=0.325, anchor=tk.CENTER)

                button_submit_update = tk.Button(popout_window, text="Submit", command=submitSection, width=20, height=2)
                button_submit_update.place(relx=0.5, rely=0.475, anchor=tk.CENTER)

                back_button = tk.Button(popout_window, text="Back", command=backButton2, width=20, height=2)
                back_button.place(relx=0.5, rely=0.625, anchor=tk.CENTER)

            def updateStudentAddress():

                def backButton2():
                    popout_window.destroy()
                    studentNewUpdate_window.deiconify()

                def submitAddress():
                    new_student_address = entry_new_address.get().strip()
                    index = 5

                    if not new_student_address:
                        messagebox.showerror("Error", "Please enter a new Address.")
                        
                    else:
                        submit_update(new_student_address, index)
                        popout_window.destroy()

                popout_window = tk.Toplevel(root)
                popout_window.title("Update Address")
                popout_window.geometry("400x350")

                label_new_student_adrs = tk.Label(popout_window, text="Enter the new Address:", font=("Helvetica", 12))
                label_new_student_adrs.pack(pady=10)

                entry_new_address = tk.Entry(popout_window, width=40)
                entry_new_address.place(relx=0.5, rely=0.325, anchor=tk.CENTER)

                button_submit_update = tk.Button(popout_window, text="Submit", command=submitAddress, width=20, height=2)
                button_submit_update.place(relx=0.5, rely=0.475, anchor=tk.CENTER)

                back_button = tk.Button(popout_window, text="Back", command=backButton2, width=20, height=2)
                back_button.place(relx=0.5, rely=0.625, anchor=tk.CENTER)

            def backButton():
                studentNewUpdate_window.destroy()
                showMainWindow()

            root.withdraw()
            studentNewUpdate_window = tk.Toplevel(root)
            studentNewUpdate_window.title("Pop-out Window1")
            studentNewUpdate_window.geometry("600x500")

            label_programTitle2 = tk.Label(studentNewUpdate_window, text="Update Student Information Records", font=("Helvetica", 16))
            label_programTitle2.place(relx=0.5, rely=0.10, anchor=tk.CENTER)

            button_updateStudentID = tk.Button(studentNewUpdate_window, text="Update Student ID", command=updateStudentID, width=40, height=2)
            button_updateStudentID.place(relx=0.5, rely=0.20, anchor=tk.CENTER)

            button_updateStudentLastName = tk.Button(studentNewUpdate_window, text="Update Student Last Name", command=updateStudentLN, width=40, height=2)
            button_updateStudentLastName.place(relx=0.5, rely=0.30, anchor=tk.CENTER)

            button_updateStudentFirstName = tk.Button(studentNewUpdate_window, text="Update Student First Name", command=updateStudentFN, width=40, height=2)
            button_updateStudentFirstName.place(relx=0.5, rely=0.40, anchor=tk.CENTER)

            button_updateStudentMiddleName = tk.Button(studentNewUpdate_window, text="Update Student Middle Name", command=updateStudentMN, width=40, height=2)
            button_updateStudentMiddleName.place(relx=0.5, rely=0.50, anchor=tk.CENTER)

            button_updateStudentSection = tk.Button(studentNewUpdate_window, text="Update Student Section", command=updateStudentSection, width=40, height=2)
            button_updateStudentSection.place(relx=0.5, rely=0.60, anchor=tk.CENTER)

            button_updateStudentAddress = tk.Button(studentNewUpdate_window, text="Update Student Address", command=updateStudentAddress, width=40, height=2)
            button_updateStudentAddress.place(relx=0.5, rely=0.70, anchor=tk.CENTER)

            button_backButton = tk.Button(studentNewUpdate_window, text="Back", command=backButton, width=40, height=2)
            button_backButton.place(relx=0.5, rely=0.80, anchor=tk.CENTER)

        else:
            messagebox.showinfo("Not Found", "Student ID not found in the records.")

    root.withdraw()
    getStudentId_window = tk.Toplevel(root)
    getStudentId_window.title("Search Student")
    getStudentId_window.geometry("600x300")

    student_id_label = tk.Label(getStudentId_window, text="Enter the student ID", font=("Helvetica", 12))
    student_id_label.place(relx=0.5, rely=0.20, anchor=tk.CENTER)

    student_id_entry = tk.Text(getStudentId_window, width=40, height=2)
    student_id_entry.place(relx=0.5, rely=0.325, anchor=tk.CENTER)

    search_button = tk.Button(getStudentId_window, text="Search", command=perform_search, width=20, height=2)
    search_button.place(relx=0.5, rely=0.475, anchor=tk.CENTER)

    back_button = tk.Button(getStudentId_window, text="Back", command=backButton1, width=20, height=2)
    back_button.place(relx=0.5, rely=0.625, anchor=tk.CENTER)

    getStudentId_window.mainloop()

#========== WINDOW FOR DELETE STUDENT ==========#
def DeleteStudent():
    getStudentIdDelete_window = tk.Tk()
    getStudentIdDelete_window.withdraw()
    student_id = simpledialog.askstring("Student ID", "Enter Student ID to delete (e.g TUPM-20-1234): ")

    if student_id:
        getStudentIdDelete_window.destroy()
        deleteStudentInfo(student_id)

    else:
        getStudentIdDelete_window.destroy()
        messagebox.showinfo("Error", "Invalid Student ID!")
        showMainWindow()


#========== EXIT MAIN MENU ==========#
def exit():
    root.destroy()

#========== WINDOW FOR MAIN MENU ==========#
root = tk.Tk()
root.title("Student Information System")
root.geometry("600x400")

label_programTitle = tk.Label(root, text="Student Information System", font=("Helvetica", 16))
label_programTitle.place(relx=0.5, rely=0.10, anchor=tk.CENTER)

#========== MAIN MENU BUTTONS ==========#
button_inputData = tk.Button(root, text="Add Student", command=AddStudent, width=20, height=2)
button_inputData.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

button_viewData= tk.Button(root, text="View Student", command=ViewStudent, width=20, height=2)
button_viewData.place(relx=0.5, rely=0.375, anchor=tk.CENTER)

button_editData = tk.Button(root, text="Update Student", command=UpdateStudent, width=20, height=2)
button_editData.place(relx=0.5, rely=0.50, anchor=tk.CENTER)

button_deleteData = tk.Button(root, text="Delete Student", command=DeleteStudent, width=20, height=2)
button_deleteData.place(relx=0.5, rely=0.625, anchor=tk.CENTER)

button_exit = tk.Button(root, text="Exit", command=exit, width=20, height=2)
button_exit.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

root.mainloop()
