import datetime

def rent_calc():
    print("price of 1 bed = Rs.500")
    print("price of 2 bed = Rs.800")
    currentDate = datetime.date.today()
    check_in = input('Please enter check-in date in format: (dd/mm/yyyy) :')
    cin = datetime.datetime.strptime(check_in, '%d/%m/%Y').date()
    print(cin)
    print(currentDate)
    days = (currentDate - cin).days
    print(days)
    ch = int(input("Enter the no. of beds in room stayed :"))
    if ch == 1:
        rent = days*500
        print("Rent = ",rent)
    elif ch == 2:
        rent = days*800
        print("Rent = ",rent)
    else:
        print("Invalid choice")
        rent_calc()
