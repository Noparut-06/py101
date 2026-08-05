num_employee = int(input("Enter the number of employee: "))
if num_employee < 50 :
    print("This is a small company.")
elif num_employee < 250 :
    print("This is a medium-size company.")
elif num_employee >= 250:
    print("This is a large company.")