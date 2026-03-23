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
s5 = Student(5, "Tina Tønnesen", {
    "IS-211": "Algorithms and Data Structures",
})

matcher.add_student(s1)
matcher.add_student(s2)
matcher.add_student(s3)
matcher.add_student(s4)

# --- Find students taking IS-211 ---
matches = matcher.match_students("IS-211")

for student in matches:
    matcher.create_study_buddy(student, "IS-211")


# --- Book students in room B2 026 --- 
room_manager.book_room("B2 026", s1)
room_manager.book_room("B2 026", s2)
room_manager.book_room("B2 026", s3)
room_manager.book_room("B2 026", s4)
room_manager.book_room("B2 026", s5)

room1.show_students()

room_manager.find_room("B2 026")

room1.remove_student(s1)

room1.show_students()

room_manager.find_room("B2 026")
                                   