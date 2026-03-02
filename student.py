<<<<<<< HEAD
class Student:
    def __init__(self, student_id, name, courses):
        self.student_id = student_id
        self.student_name = name
        self.courses = courses
        self.study_buddies = []

    def add_study_buddy(self, buddy):
        self.study_buddies.append(buddy)

    def get_courses(self):
        return self.courses

    def list_courses(self):
        print(f"\nList of courses for {self.student_name}:")

        sorted_courses = sorted(self.courses.items())

        for code, course_name in sorted_courses:
            print(f"{code}: {course_name}")
        return sorted_courses

    def show_study_buddies(self):
        print(f"\nList of buddies for {self.student_name}:")

        if not self.study_buddies:
            print("No buddies found")
            return

        sorted_buddies = sorted(
            self.study_buddies,
            key=lambda buddy: buddy.student_name
        )
        for study_buddy in sorted_buddies:
=======
class Student:
    def __init__(self, student_id, name, courses):
        self.student_id = student_id
        self.student_name = name
        self.courses = courses
        self.study_buddies = []

    def add_study_buddy(self, buddy):
        self.study_buddies.append(buddy)

    def get_courses(self):
        return self.courses

    def list_courses(self):
        print(f"\nList of courses for {self.student_name}:")

        sorted_courses = sorted(self.courses.items())

        for code, course_name in sorted_courses:
            print(f"{code}: {course_name}")
        return sorted_courses

    def show_study_buddies(self):
        print(f"\nList of buddies for {self.student_name}:")

        if not self.study_buddies:
            print("No buddies found")
            return

        sorted_buddies = sorted(
            self.study_buddies,
            key=lambda buddy: buddy.student_name
        )
        for study_buddy in sorted_buddies:
>>>>>>> 938412a (første kode til Study Buddy)
            print(f"{study_buddy.student_name} - Course(s) {study_buddy.courses})")