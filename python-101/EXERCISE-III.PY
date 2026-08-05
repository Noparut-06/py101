rows = int(input("Enter rows: "))
for i in range(1,101) :
    print(i, end="\t")
    if i % rows ==0:
        print()