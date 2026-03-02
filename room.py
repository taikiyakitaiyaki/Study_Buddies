<<<<<<< HEAD
from collections import deque

class Room:
    def __init__(self, room_id, capacity):
        self.room_id = room_id
        self.capacity = capacity
        self.students = []
        self.queue = deque()

    """Checking if room is full"""
    def is_full(self):
        return len(self.students) >= self.capacity

    """Adding student to room if is available, queue if not"""
    def add_student(self, student):
        if student in self.students:
            print(f"\n{student.student_name} is already booked in {self.room_id}.")
            return False
        if student in self.queue:
            print(f"\n{student.student_name} is already in the waiting list for room {self.room_id}.")
            return False

        if not self.is_full():
            self.students.append(student)
            print(f"\n{student.student_name} is now booked in room {self.room_id}.")
            return True
        else:
            self.add_to_queue(student)
            print(f"{self.room_id} is full. {student.student_name} is added to the waiting list.")
            return False

    """adding student to waiting list"""
    def add_to_queue(self, student):
        self.queue.append(student)

    """remove student from waiting list, and adding the next one in line"""
    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"{student.student_name} removed from {self.room_id}.")
        else:
            print(f"{student.student_name} not in {self.room_id}.")

    """adding next student to room if available"""
    def next_on_queue(self):
        if self.queue and not self.is_full():
            next_student = self.queue.popleft()
            self.add_student(next_student)
            print(f"{next_student.student_name} moved from queue to room {self.room_id}.")
            return next_student
        return None

    """show all students that have booked rooms"""
    def show_students(self):
        if self.students:
            print(f"\nStudents in {self.room_id}:")
            for student in self.students:
                print(f"{student.student_name}")
        else:
            print(f"\nNo students in {self.room_id}")

        if self.queue:
            print("Waiting list:")
            for student in self.queue:
=======
from collections import deque

class Room:
    def __init__(self, room_id, capacity):
        self.room_id = room_id
        self.capacity = capacity
        self.students = []
        self.queue = deque()

    """Checking if room is full"""
    def is_full(self):
        return len(self.students) >= self.capacity

    """Adding student to room if is available, queue if not"""
    def add_student(self, student):
        if student in self.students:
            print(f"\n{student.student_name} is already booked in {self.room_id}.")
            return False
        if student in self.queue:
            print(f"\n{student.student_name} is already in the waiting list for room {self.room_id}.")
            return False

        if not self.is_full():
            self.students.append(student)
            print(f"\n{student.student_name} is now booked in room {self.room_id}.")
            return True
        else:
            self.add_to_queue(student)
            print(f"{self.room_id} is full. {student.student_name} is added to the waiting list.")
            return False

    """adding student to waiting list"""
    def add_to_queue(self, student):
        self.queue.append(student)

    """remove student from waiting list, and adding the next one in line"""
    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"{student.student_name} removed from {self.room_id}.")
        else:
            print(f"{student.student_name} not in {self.room_id}.")

    """adding next student to room if available"""
    def next_on_queue(self):
        if self.queue and not self.is_full():
            next_student = self.queue.popleft()
            self.add_student(next_student)
            print(f"{next_student.student_name} moved from queue to room {self.room_id}.")
            return next_student
        return None

    """show all students that have booked rooms"""
    def show_students(self):
        if self.students:
            print(f"\nStudents in {self.room_id}:")
            for student in self.students:
                print(f"{student.student_name}")
        else:
            print(f"\nNo students in {self.room_id}")

        if self.queue:
            print("Waiting list:")
            for student in self.queue:
>>>>>>> 938412a (første kode til Study Buddy)
                print(f"{student.student_name}")