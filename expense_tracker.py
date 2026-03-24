# expense tracker 

expense = [] 
while True:
    print("press(1) to add an expense.")
    print("press(2) to view expense.")
    print("press(3) to show the total expense.")
    print("press(4) to exit.")

    choice = input("choose a number please: ")

    if choice =="4":
        print("exit sucessfull")
        break
    elif choice == "3":
        print("option 3 selected to show the total expense")
        total = sum(item[1] for item in expense)
        print(f"your total expense is: ${total}")
    
    elif choice == "2":
        print("option 2 selected to view the expense")
        
        for category, amount in expense:
                print(f"Category: {category} | Amount: ${amount}")
        
    elif choice == "1":
        print("option 1 selected to add an expense")
        catagory = input("please enter the catagory you spent money upon: ")
        amount = float(input(f"please enter the amount you spent on {catagory}: "))
        expense.append((catagory, amount))

        #save the expense in expense.txt

        with open("expense.txt", "a") as f:
            f.write(f"{catagory}: ${ amount}\n")

        print("expense addition successfull.\nTHANK you")
        

    else:
        print("invalid input please try again select number 1 - 4")
    

         