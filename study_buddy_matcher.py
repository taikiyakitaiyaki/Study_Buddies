<<<<<<< HEAD
class StudyBuddyMatcher:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def match_students(self, course_code):
        matched = []
        for student in self.students.values():
            if course_code in student.courses:
                matched.append(student)
        return matched

    def create_study_buddy(self, student, course_code):
        matches = self.match_students(course_code)

        for buddy in matches:
            if buddy != student:
                student.add_study_buddy(buddy)

=======
class StudyBuddyMatcher:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def match_students(self, course_code):
        matched = []
        for student in self.students.values():
            if course_code in student.courses:
                matched.append(student)
        return matched

    def create_study_buddy(self, student, course_code):
        matches = self.match_students(course_code)

        for buddy in matches:
            if buddy != student:
                student.add_study_buddy(buddy)

>>>>>>> 938412a (første kode til Study Buddy)
