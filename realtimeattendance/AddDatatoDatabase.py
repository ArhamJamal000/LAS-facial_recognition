import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendacerealtime-8ca17-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

# Specify the number of times to add new dictionaries
n = int(input("Enter the number of dictionaries to add: "))

for _ in range(n):
    # Specify the new outer key and inner values at runtime
    new_outer_key = input("Enter the Roll Number: ")
    new_name = input("Enter the Name: ")
    new_branch = input("Enter the Branch: ")
    new_starting_year = int(input("Enter the Starting Year: "))
    new_total_attendance = int(input("Enter the Total Attendance: "))
    new_section = input("Enter the Section: ")
    new_year = int(input("Enter the Year: "))

    # Getting the current time in the desired format
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Creating a new dictionary for the current entry
    new_entry = {
        "name": new_name,
        "branch": new_branch,
        "starting_year": new_starting_year,
        "total_attendance": new_total_attendance,
        "section": new_section,
        "year": new_year,
        "last_attendance_time": current_time
    }

    # Adding the new entry to the database under the specified roll number
    ref.child(new_outer_key).set(new_entry)

    print("Entry added to the database")

# No need to set the entire dictionary to Firebase outside the loop
