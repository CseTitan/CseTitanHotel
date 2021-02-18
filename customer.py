from datetime import datetime
from organize_menu import print_bar


class Customer:
    def __init__(self, customer_id, name, address, phone, room_no, entry_date, checkout_date):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.phone = phone
        self.room_no = room_no
        self.entry_date = entry_date
        self.checkout_date = checkout_date

    def print_all(self):
        print(str(self.customer_id).ljust(3),
              self.name[0:15].ljust(15),
              self.address[0:15].ljust(15),
              self.phone.ljust(15),
              str(self.room_no).ljust(10),
              self.entry_date.strftime("%d-%b-%y").ljust(15),
              (self.checkout_date.strftime("%d %b %y") if self.checkout_date is not None else "None").ljust(15))

    def print_full(self):
        print_bar()
        print("Customer #", self.customer_id)
        print("Name: ", self.name)
        print("Address: ", self.address)
        print("Phone: ", self.phone)
        print("Checked in to room #", self.room_no, " on ", self.entry_date.strftime("%d %b %y"))
        print("Checkout: ", self.checkout_date.strftime("%d %b %y") if self.checkout_date is not None else None)
        print_bar()


def create_customer(customer_id, room_no):
    name = input("Enter the name: ")
    address = input("Enter the address: ")
    phone = input("Enter the phone: ")
    entry_date = datetime.now()
    return Customer(customer_id, name, address, phone, room_no, entry_date, None)


def print_header():
    print("="*100)
    print("id".ljust(3),
          "name".ljust(15),
          "address".ljust(15),
          "phone".ljust(15),
          "room no".ljust(10),
          "entry".ljust(15),
          "check out".ljust(15))
    print("="*100)
