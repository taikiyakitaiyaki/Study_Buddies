<<<<<<< HEAD
class RoomManager:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.room_id] = room
        print(f"Room {room.room_id} added.")

    def find_room(self, room_id):
        room = self.rooms.get(room_id)
        if room:
            print(f"\nRoom {room_id} - Capacity: {room.capacity}, Booked: {len(room.students)}, Waiting: {len(room.queue)}")
        else:
            print(f"\nRoom {room_id} not found.")
        return room

    def book_room(self, room_id, student):
        room = self.rooms.get(room_id)
        if room:
            room.add_student(student)
            # print(f"Room {room_id} booked")
        else:
            print(f"Room {room_id} not found.")

    def remove_student_from_room(self, room_id, student):
        room = self.rooms.get(room_id)
        if room:
            room.remove_student(student)
        else:
            print(f"Room {room_id} not found.")

    def add_to_queue(self, room_id, student_id):
        room = self.rooms.get(room_id)
        if room:
            room.add_to_queue(student_id)
            print(f"Student {student_id} added to queue for room {room.room_id}.")
            return True
        else:
            print(f"Room {room_id} not found.")
=======
class RoomManager:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.room_id] = room
        print(f"Room {room.room_id} added.")

    def find_room(self, room_id):
        room = self.rooms.get(room_id)
        if room:
            print(f"\nRoom {room_id} - Capacity: {room.capacity}, Booked: {len(room.students)}, Waiting: {len(room.queue)}")
        else:
            print(f"\nRoom {room_id} not found.")
        return room

    def book_room(self, room_id, student):
        room = self.rooms.get(room_id)
        if room:
            room.add_student(student)
            # print(f"Room {room_id} booked")
        else:
            print(f"Room {room_id} not found.")

    def remove_student_from_room(self, room_id, student):
        room = self.rooms.get(room_id)
        if room:
            room.remove_student(student)
        else:
            print(f"Room {room_id} not found.")

    def add_to_queue(self, room_id, student_id):
        room = self.rooms.get(room_id)
        if room:
            room.add_to_queue(student_id)
            print(f"Student {student_id} added to queue for room {room.room_id}.")
            return True
        else:
            print(f"Room {room_id} not found.")
>>>>>>> 938412a (første kode til Study Buddy)
        return False