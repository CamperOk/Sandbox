i= input("Please enter anything ")
if i.isdigit():
    if int(i) % 2 == 0:
        print(i, "is an even number.")
    else:
        print(i,"is an odd number.")
else:
    print(i, "Is a text or combined value")