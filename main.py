<<<<<<< HEAD
from student import Student
from courses import Courses
from room import Room
from room_manager import RoomManager
from study_buddy_matcher import StudyBuddyMatcher

def create_student():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    courses = Courses.choose_courses()

    return Student(student_id, student_name, courses)

# --- Create managers ---
matcher =StudyBuddyMatcher()
room_manager = RoomManager()

# --- Create rooms ---
room1 = Room("B2 026", 4)
room2 = Room("B2 024", 4)
room3 = Room("B2 029", 6)
room4 = Room("B3 002", 10)
room5 = Room("F1 001", 4)
room6 = Room("F1 003", 8)
room7 = Room("F1 004", 10)
room8 = Room("F2 022", 6)

room_manager.add_room(room1)
room_manager.add_room(room2)
room_manager.add_room(room3)
room_manager.add_room(room4)
room_manager.add_room(room5)
room_manager.add_room(room6)
room_manager.add_room(room7)
room_manager.add_room(room8)

# --- Create students ---

s1 = Student(1, "Tom Stiansen", {
    "IS-211": "Algorithms and Data Structures",
    "IS-110": "Objektorientert programmering",
    "IS-214": "Information Systems Security",
    })
s2 = Student(2, "Jorunn Pedersen", {
    "IS-211": "Algorithms and Data Structures",
    "IS-214": "Information Systems Security",
    })
s3 = Student(3, "Jimmy Pripp", {"IS-211": "Algorithms and Data Structures"})
s4 = Student(4, "Anna Bonanza", {
    "BE-111": "Innføring i finansregnskap",
    "SE-204": "Makroøkonomi"
    })

matcher.add_student(s1)
matcher.add_student(s2)
matcher.add_student(s3)
matcher.add_student(s4)

print("\nStudents taking IS-211:")
matches = matcher.match_students("IS-211")

for student in matches:
    print(student.student_name)

matcher.create_study_buddy(s1, "IS-211")
s1.show_study_buddies()

room_manager.book_room("B2 026", s1,)
room_manager.book_room("B2 026", s1,)


=======
from student import Student
from courses import Courses
from room import Room
from room_manager import RoomManager
from study_buddy_matcher import StudyBuddyMatcher

def create_student():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    courses = Courses.choose_courses()

    return Student(student_id, student_name, courses)

# --- Create managers ---
matcher =StudyBuddyMatcher()
room_manager = RoomManager()

# --- Create rooms ---
room1 = Room("B2 026", 4)
room2 = Room("B2 024", 4)
room3 = Room("B2 029", 6)
room4 = Room("B3 002", 10)
room5 = Room("F1 001", 4)
room6 = Room("F1 003", 8)
room7 = Room("F1 004", 10)
room8 = Room("F2 022", 6)

room_manager.add_room(room1)
room_manager.add_room(room2)
room_manager.add_room(room3)
room_manager.add_room(room4)
room_manager.add_room(room5)
room_manager.add_room(room6)
room_manager.add_room(room7)
room_manager.add_room(room8)

# --- Create students ---

s1 = Student(1, "Tom Stiansen", {
    "IS-211": "Algorithms and Data Structures",
    "IS-110": "Objektorientert programmering",
    "IS-214": "Information Systems Security",
    })
s2 = Student(2, "Jorunn Pedersen", {
    "IS-211": "Algorithms and Data Structures",
    "IS-214": "Information Systems Security",
    })
s3 = Student(3, "Jimmy Pripp", {"IS-211": "Algorithms and Data Structures"})
s4 = Student(4, "Anna Bonanza", {
    "BE-111": "Innføring i finansregnskap",
    "SE-204": "Makroøkonomi"
    })

matcher.add_student(s1)
matcher.add_student(s2)
matcher.add_student(s3)
matcher.add_student(s4)

print("\nStudents taking IS-211:")
matches = matcher.match_students("IS-211")

for student in matches:
    print(student.student_name)

matcher.create_study_buddy(s1, "IS-211")
s1.show_study_buddies()

room_manager.book_room("B2 026", s1,)
room_manager.book_room("B2 026", s1,)


>>>>>>> 938412a (første kode til Study Buddy)
room1.is_full()