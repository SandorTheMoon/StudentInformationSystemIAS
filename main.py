# Group Members:
# Castro, Patrick Josuah B.
# Corpuz, Mark Jhay
# Deang, April Joy L.
# Espero, Airysh Xander M.

# New codes:
import tkinter as tk
import os

root = tk.Tk()
root.title("Student Information System")
root.geometry("600x400")

label_programTitle = tk.Label(root, text="Student Information System", font=("Helvetica", 16))
label_programTitle.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

def inputData():
    root.destroy()
    label = tk.Label(root, text="Student ID:")
    label.pack(pady=10)
    label = tk.Label(root, text="First Name:")
    label.pack(pady=10)
    label = tk.Label(root, text="Middle Name:")
    label.pack(pady=10)
    label = tk.Label(root, text="Section:")
    label.pack(pady=10)
    label = tk.Label(root, text="Address:")
    label.pack(pady=10)

button_inputData = tk.Button(root, text="Input Data", command=inputData, width=20, height=2)
button_inputData.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

button_viewData= tk.Button(root, text="View Data", command=inputData, width=20, height=2)
button_viewData.place(relx=0.5, rely=0.50, anchor=tk.CENTER)

root.mainloop()

# The codes below are Sandor's codes.

# def encryptData(data):
#     key = 4
#     return ''.join(chr(ord(letter) + key) for letter in data)

# def decryptData(encryptedData):
#     key = 4
#     return ''.join(chr(ord(letter) - key) for letter in encryptedData)

# def addStudentInfo(student_data):
#     with open("Students.txt", "a") as file:
#         file.write(','.join(student_data) + '\n')

# def displayStudentInfo(studID):
#     with open("Students.txt", "r") as file:
#         for line in file:
#             keyValue = line.strip().split(",")
#             if keyValue[0] == studID:
#                 decrypted_data = [decryptData(data) for data in keyValue]
#                 os.system("cls")
#                 print("--- Student Info ---")
#                 print(f"Student ID: {decrypted_data[0]}")
#                 print(f"Name: {decrypted_data[1]}, {decrypted_data[2]} {decrypted_data[3]}")
#                 print(f"Section: {decrypted_data[4]}")
#                 print(f"Address: {decrypted_data[5]}")
#                 return
#         os.system("cls")
#         print("Student not found or invalid input.")

# while True:
#     try:
#         os.system("cls")
#         print("--- Student Information System ---")
#         print("1. Input Data")
#         print("2. View Data")
#         choice = int(input("Choose option: "))

#         if choice == 1:
#             os.system("cls")
#             print("--- Add Student Information ---")
#             studentId = encryptData(input("Student ID: "))
#             lastName = encryptData(input("Last Name: "))
#             firstName = encryptData(input("First Name: "))
#             midName = encryptData(input("Middle Name: "))
#             section = encryptData(input("Section: "))
#             address = encryptData(input("Address: "))
#             addStudentInfo([studentId, lastName, firstName, midName, section, address])
#             print("Student added...")
#             os.system("pause")

#         elif choice == 2:
#             os.system("cls")
#             print("--- Find Student Information ---")
#             getStudentId = encryptData(input("Enter Student ID (e.g TUPM-20-1234): "))
#             displayStudentInfo(getStudentId)
#             os.system("pause")

#         else:
#             os.system("cls")
#             print("Invalid option!")
#             os.system("pause")
    
#     except ValueError:
#         os.system("cls")
#         print("Invalid input!")
#         os.system("pause")
