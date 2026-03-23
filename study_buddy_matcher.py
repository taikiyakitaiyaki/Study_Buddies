class StudyBuddyMatcher:
    def __init__(self):
        self.students = {} # id -> Student

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
            if buddy is student:
                continue
            if buddy not in student.study_buddies:
                student.add_study_buddy(buddy)
            if student not in buddy.study_buddies:
                buddy.add_study_buddy(student)

