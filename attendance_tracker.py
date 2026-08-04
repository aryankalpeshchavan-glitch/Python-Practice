"""
attendance_tracker.py

Purpose:
    A simple Class Attendance Tracker for a faculty member to mark daily
    attendance for a class and compute attendance percentages.

    Concepts used: variables, input/output, lists, dictionaries,
    loops, and if-else statements.

Name: Aryan Chavan
Roll No: 25108A0066
"""

import os
import json

DATA_FILE = "attendance_data.json"
AT_RISK_THRESHOLD = 75  # percentage below which a student is "At Risk"


def get_student_names(num_students):
    """Ask the user for each student's name and return a list of names."""
    names = []
    for i in range(1, num_students + 1):
        name = input(f"Enter name of student {i}: ").strip()
        names.append(name)
    return names


def mark_attendance(student_names, attendance_data):
    """
    Ask, for each student, whether they are present today.
    Increments attendance_data[name] by 1 if present.
    Returns (total_present, total_absent) for the day.
    """
    total_present = 0
    total_absent = 0

    print("\n--- Marking Today's Attendance ---")
    for name in student_names:
        response = input(f"Is {name} present today? (Y/N): ").strip().upper()

        if response == "Y":
            attendance_data[name] += 1
            total_present += 1
        else:
            total_absent += 1

    return total_present, total_absent


def compute_percentage(days_present, total_classes):
    """Compute attendance percentage for one student."""
    if total_classes == 0:
        return 0.0
    return (days_present / total_classes) * 100


def display_summary(course_name, division, student_names, attendance_data,
                     total_classes, total_present, total_absent):
    """Print a formatted attendance summary table."""
    print("\n===================================")
    print(f"Course     : {course_name}")
    print(f"Division   : {division}")
    print(f"Total Classes Conducted: {total_classes}")
    print("===================================")

    print(f"{'Name':<20}{'Days Present':<15}{'Attendance %':<15}{'Status':<10}")
    print("-" * 60)

    for name in student_names:
        days_present = attendance_data[name]
        percentage = compute_percentage(days_present, total_classes)
        status = "At Risk" if percentage < AT_RISK_THRESHOLD else "OK"
        print(f"{name:<20}{days_present:<15}{percentage:<15.2f}{status:<10}")

    print("-" * 60)
    print(f"Total Present Today : {total_present}")
    print(f"Total Absent Today  : {total_absent}")
    print("===================================\n")


def save_attendance_data(course_name, division, student_names,
                          attendance_data, total_classes):
    """Save attendance data to a JSON file for persistence across runs."""
    data = {
        "course_name": course_name,
        "division": division,
        "student_names": student_names,
        "attendance_data": attendance_data,
        "total_classes": total_classes,
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Attendance data saved to '{DATA_FILE}'.")


def load_attendance_data():
    """Load attendance data from the JSON file, if it exists."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return None


if __name__ == "__main__":
    print("=======================================================")
    print("      CLASS ATTENDANCE TRACKER")
    print("  Mark daily attendance and view attendance summary")
    print("=======================================================\n")

    # ---------- Part 2: Initializing Class and Student List ----------
    saved_data = None
    use_saved = input(
        "Load existing attendance data from file, if available? (Y/N): "
    ).strip().upper()

    if use_saved == "Y":
        saved_data = load_attendance_data()

    if saved_data:
        course_name = saved_data["course_name"]
        division = saved_data["division"]
        student_names = saved_data["student_names"]
        attendance_data = saved_data["attendance_data"]
        total_classes = saved_data["total_classes"]
        print(f"\nLoaded data for {course_name} - {division} "
              f"({total_classes} classes so far).\n")
    else:
        course_name = input("Enter course name (e.g., Python Programming): ").strip()
        division = input("Enter division (e.g., FE CMPN A): ").strip()

        while True:
            try:
                num_students = int(input("Enter number of students in the class: "))
                if num_students > 0:
                    break
                print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

        student_names = get_student_names(num_students)

        # Dictionary: key = student name, value = number of days present
        attendance_data = {name: 0 for name in student_names}
        total_classes = 0

    # ---------- Part 3 & 6: Marking Attendance (possibly multiple days) ----------
    keep_going = True
    while keep_going:
        total_present, total_absent = mark_attendance(student_names, attendance_data)
        total_classes += 1

        # ---------- Part 5: Displaying the Attendance Summary ----------
        display_summary(course_name, division, student_names, attendance_data,
                         total_classes, total_present, total_absent)

        # ---------- Part 6: Optional multi-day loop ----------
        another_day = input(
            "Do you want to mark attendance for another day? (Y/N): "
        ).strip().upper()
        keep_going = (another_day == "Y")

    # ---------- Part 6: Save data for persistence across runs ----------
    save_choice = input("Save attendance data to file for next time? (Y/N): ").strip().upper()
    if save_choice == "Y":
        save_attendance_data(course_name, division, student_names,
                              attendance_data, total_classes)

    print("Thank you for using the Class Attendance Tracker. Goodbye!")