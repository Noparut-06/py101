keep_going = 'y'
while keep_going == 'y' :
    cost = float(input("Enter the item's Wholesalae cost : "))
    comm_rate = float(input("Enter the commission rate : "))
    retail_price = wholes * 2.5
    print(f'The commission is ${commission:.2f}')
    keep_going = input('Do you want to calculate another' +  'commission (Enter y for yes): ')
