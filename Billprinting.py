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
    nextcustomer=input("Do you want to go to next customer?(Yes/No)")
    if nextcustomer=="no" or nextcustomer=="No":
        break
