import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": 'https://faceattendancerealtime-fc1e2-default-rtdb.firebaseio.com/'
})

ref = db.reference('Students')

def add_record(key, name, major, starting_year, total_attendance, standing, year, last_attendance_time):
    data = {
        "Name": name,
        "Major": major,
        "Starting_Year": starting_year,
        "Total_Attendance": total_attendance,
        "Standing": standing,
        "Year": year,
        "Last_Attendance_Time": last_attendance_time
    }
    ref.child(key).set(data)

def update_record(key, field, value):
    ref.child(key).update({field: value})

# Example usage
add_record("19037", "Ishita Saini", "CSE", 2019, 4, "G", 4, "2023-03-09 00:50:34")
add_record("19802", "Nikhil Badoni ", "CSE", 2019, 8, "VG", 4, "2023-03-09 00:50:34")
add_record("191322", "Shubham Kumar Bhatt ", "CSE", 2019, 6, "VG", 4, "2023-03-09 00:50:34")

# update_record("19037", "Total_Attendance", 6)
