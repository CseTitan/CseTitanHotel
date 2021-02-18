from storage import DataFile
from room import create_room, print_header


NUMBER_OF_RECORDS_PER_PAGE = 10
roomTable = DataFile("roomdata.dat")


def add_room():
    rooms = roomTable.get_records()
    if len(rooms) == 0:
        room_id = 0
    else:
        room_id = rooms[len(rooms) - 1].room_id + 1
    room = create_room(room_id)
    roomTable.add_record(room)
    print("Room Added")


def get_and_print_room_by_no():
    rooms = roomTable.get_records()
    found = False
    position = -1
    if len(rooms) == 0:
        print("No Record found")
    else:
        room_no = int(input("Enter the room no: "))
        for room in rooms:
            position += 1
            if room_no == room.room_no:
                found = True
                break
        if not found:
            print("No matching record")
        else:
            rooms[position].print_full()
    return rooms, found, position


def get_and_print_room_by_beds():
    rooms = roomTable.get_records()
    results = []
    if len(rooms) == 0:
        print("No Records found")
    else:
        beds = int(input("Enter the number of required beds: "))
        for room in rooms:
            if beds == room.beds:
                results.append(room)
        if len(results) == 0:
            print("No matching record")
        else:
            print(len(results), " matching records")
            print_header()
            for room in results:
                room.print_all()
    return results


def edit_room_details():
    rooms, found, position = get_and_print_room_by_no()
    if found:
        room = rooms[position]
        print("Input new values (leave blank to keep previous value)")
        room_no = input("Enter new room no: ")
        if len(room_no) > 0:
            room.room_no = int(room_no)
        floor = input("Enter new floor: ")
        if len(floor) > 0:
            room.floor = floor
        beds = input("Enter number of beds: ")
        if len(beds) > 0:
            room.beds = int(beds)
        roomTable.overwrite(rooms)
        print("Details Updated ")


def delete_room():
    rooms, found, position = get_and_print_room_by_no()
    if found:
        room = rooms[position]
        print("Delete this room ? (Y/N) : ")
        confirm = input()
        if confirm.lower() == 'y':
            rooms.remove(room)
            roomTable.overwrite(rooms)
            print("Room Deleted")
        else:
            print("Operation Canceled")


def change_room_status(room_no, available):
    rooms = roomTable.get_records()
    found = False
    position = -1
    if len(rooms) == 0:
        print("No Record found")
    else:
        for room in rooms:
            position += 1
            if room_no == room.room_no:
                found = True
                break
        if not found:
            print("No matching record")
        else:
            room = rooms[position]
            room.available = available
            roomTable.overwrite(rooms)
            print("Room Status Changed")


def view_all_rooms():
    rooms = roomTable.get_records()
    if len(rooms) == 0:
        print("No Record found")
    else:
        i = 0
        print_header()
        for room in rooms:
            i += 1
            room.print_all()
            if i == NUMBER_OF_RECORDS_PER_PAGE:
                input("Press any key to continue.")


def room_menu():
    while True:
        print()
        print("============================")
        print("==========Room Menu=========")
        print("============================")
        print()

        print("1. Add new room")
        print("2. Get room details by room no")
        print("3. Find available rooms by number of beds")
        print("4. Edit Room details")
        print("5. Delete room")
        print("6. View all rooms")
        print("0. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_room()
        elif choice == 2:
            get_and_print_room_by_no()
        elif choice == 3:
            get_and_print_room_by_beds()
        elif choice == 4:
            edit_room_details()
        elif choice == 5:
            delete_room()
        elif choice == 6:
            view_all_rooms()
        elif choice == 0:
            break
        else:
            print("Invalid choice (Press 0 to go back)")
