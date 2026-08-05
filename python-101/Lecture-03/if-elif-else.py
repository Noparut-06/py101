inchar = input("Input one character: ")
if inchar >= 'A' and inchar <= 'Z' :
    print("You in put upper case Letter ", inchar)
elif inchar >= 'a' and inchar <= 'z' :
    print("You in put Lower case Letter ", inchar)
elif inchar >= '0' and inchar <= "9" :
    print("You in put Number ",inchar)
else :
    print("Is's not a letter or number.",inchar)