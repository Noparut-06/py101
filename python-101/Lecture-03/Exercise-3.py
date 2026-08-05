hours_worked = int(input("Enter the number of hours worked: "))
pay_rate = int(input("Enter the hourly pay rate: "))
if hours_worked <= 40 :
    gross_pay = hours_worked*pay_rate
else:
    regular_pay = 40 * pay_rate    