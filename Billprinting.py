while True:
    Name=input("Enter Customer Name:")
    total=0
    while True:
        print("Enter Amount And Quentity")
        amount=float(input("Enter Amount:"))
        quentity=float(input("Enter Quentity:"))
        total += amount*quentity
        repet=input("Do you want to add more items?(Yes/No)")
        if repet=="no:" or repet=="no":
            break
    print("----------------------------")
    print("Name",Name)
    print("Amount to be paid",total)
    print("----------------------------")
    print("***** Happy Shopping *****")
    print("***** Visit Us Again *****")
    repet1=input("Do you want to go to next customer?(Yes/No)")
    if repet1=="no" or repet1=="No":
        break
