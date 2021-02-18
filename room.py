from organize_menu import print_bar


class Room:
    def __init__(self, room_id, room_no, floor, beds, available):
        self.room_id = room_id
        self.room_no = room_no
        self.floor = floor
        self.beds = beds
        self.available = available

    def print_all(self):
        print(str(self.room_id).ljust(3),
              str(self.room_no).ljust(15),
              self.floor.ljust(15),
              str(self.beds).ljust(15),
              str(self.available).ljust(15))

    def print_full(self):
        print_bar()
        print("Record #", self.room_id)
        print("Room No: ", self.room_no)
        print("Floor: ", self.floor)
        print("Beds: ", self.beds)
        print("available: ", self.available)
        print_bar()


def create_room(room_id):
    room_no = int(input("Enter the room no: "))
    floor = input("Enter the floor (Ex. ground, first etc.): ")
    beds = int(input("Enter number of beds: "))
    available = True
    return Room(room_id, room_no, floor, beds, available)


def print_header():
    print("="*100)
    print("id".ljust(3),
          "room no".ljust(15),
          "floor".ljust(15),
          "beds".ljust(15),
          "available".ljust(15)
          )
    print("="*100)
