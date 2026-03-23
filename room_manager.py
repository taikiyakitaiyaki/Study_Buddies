class RoomManager:
    def __init__(self):
        self.rooms = {}

    # Add a room
    def add_room(self, room):
        self.rooms[room.room_id] = room
        print(f"Room {room.room_id} added.")

    # Find a room by its ID and display its status
    def find_room(self, room_id):
        room = self.rooms.get(room_id)
        if room:
            print(f"\nRoom {room_id} - Capacity: {room.capacity}, Booked: {len(room.students)}, Waiting: {len(room.queue)}")
        else:
            print(f"\nRoom {room_id} not found.")
        return room

    # Book a student into a room
    def book_room(self, room_id, student):
        room = self.rooms.get(room_id)
        if room:
            room.add_student(student)
            student.booked_room = room
        else:
            print(f"Room {room_id} not found.")

    # Remove a student from a room
    def remove_student_from_room(self,room_id, student):
        room = self.rooms.get(room_id)
        if room:
            room.remove_student(student)
        else:
            print(f"Room {room_id} not found.")

    # Add a student to the waiting queue of a room
    def add_to_queue(self, room_id, student):
        room = self.rooms.get(room_id)
        if room:
            room.add_to_queue(student)
            print(f"Student {student.student_name} added to queue for room {room.room_id}.")
            return True
        else:
            print(f"Room {room_id} not found.")
            return False
