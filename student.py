class Student:
    def __init__(self, student_id, name, courses):
        self.student_id = student_id
        self.student_name = name
        self.courses = courses #dictionary: code -> name
        self.booked_room = None
        self.study_buddies = []

    def add_study_buddy(self, buddy):
        if buddy not in self.study_buddies:
            self.study_buddies.append(buddy)


    def list_courses(self):
        sorted_courses = sorted(self.courses.items())
        print(f"\nList of courses for {self.student_name}:")
        for code, course_name in sorted_courses:
            print(f"{code}: {course_name}")
        return sorted_courses

    def show_study_buddies(self):
        if not self.study_buddies:
            print("No buddies found")
            return

        sorted_buddies = sorted(
            self.study_buddies,
            key=lambda buddy: buddy.student_name
        )
        print(f"\nList of buddies for {self.student_name}:")
        for study_buddy in sorted_buddies:
            if study_buddy.booked_room:
                print(f"{study_buddy.student_name} - Course(s) {study_buddy.courses}.")
            else:
                print(f"{study_buddy.student_name} - Course(s) {study_buddy.courses}.")

    """show buddies room"""
    def show_buddy_room(self, buddy):

        if buddy == self:
            print(f"You cannot check yourself as a buddy.")
            return
        if buddy not in self.study_buddies:
            print(f"{buddy.student_name} is not your study buddy.")
            return

        if buddy.booked_room is None:
            print(f"Your buddy {buddy.student_name} had not booked a room")
        else:
            print(f"Your buddy {buddy.student_name} booked room {buddy.booked_room.room_id}")