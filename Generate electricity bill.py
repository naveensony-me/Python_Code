
def calculate_bill(units):
    if units <= 100:
        bill = 0
    elif units <= 400:
        bill = (units - 100) * 2
    else:
        bill = 300 * 2 + (units - 400) * 5
    return bill

units = int(input("Enter the number of electric units consumed: "))
if units < 0:
    print("Please enter a valid number of units.")
else:
    total_bill = calculate_bill(units)
    print("Total bill: Rs", total_bill)










    
