
#TODO Easy Tasks
#! Task 1: Rocket Launch
#* Print a countdown from 10 to 1 using a loop, then print "Liftoff!" after the loop ends. 

def rocket_launch():
    for i in range(0, 10):
        print(10 - i)
    print("Liftoff!")

#! Task 2: Cinema Tickets
#* A cinema has 5 visitors in the queue. Ask for the age of each visitor one by one. Anyone under 18 
#* gets a child ticket, everyone else gets an adult ticket. At the end print how many child tickets and 
#* how many adult tickets were sold.

def cinema_tickets():
    child_tickets = 0
    adult_tickets = 0
    for i in range(0, 5):
        age = int(input(f"Enter the age of visitor {i + 1}: "))
        if age < 18:
            child_tickets += 1
        else:
            adult_tickets += 1
    print(f"Child tickets sold: {child_tickets}")
    print(f"Adult tickets sold: {adult_tickets}")

#! Task 3: Read the Code
#* output: 1 3 5 7 9

#! Task 4: Shopping basket
#*Ask the user for the price of 5 items. After the fifth item, print the total and the average price.

def shopping_basket():
    total_price = 0
    for i in range(5):
        price = float(input(f"Enter the price of item {i + 1}: "))
        total_price += price
    average_price = total_price / 5
    print(f"Total price: {total_price}")
    print(f"Average price: {average_price}")

#! Task 5: Choose a password
#* Ask the user to create a password. If it is shorter than 8 characters, print "Too short, try again" and 
#* ask again. Keep asking until the password is long enough, then print "Password accepted".

def choose_password():
    while True:
        password = input("Create a password: ")
        if len(password) < 8:
            print("Too short, try again.")
        else:
            print("Password accepted.")
            break

#! Task 6: Read the code
#* output: 70 40 10 -20 Done

#! Task 7: Step counter
#*A fitness app records 1200 steps every day. Print the total number of steps after each day for one 
#*week (7 days). 

def step_counter():
    daily_steps = 1200
    total_steps = 0
    for day in range(1, 8):
        total_steps += daily_steps
        print(f"Total steps after day {day}: {total_steps}")

#! Task 8: Simple login
#* The correct username is admin and the correct password is 1234. Ask the user for a username and 
#* password. If both are correct, print "Welcome!" and stop. If not, print "Wrong username or 
#* password" and let them try again. The user has 3 attempts in total. After the third wrong attempt 
#* print "Account locked". 

def simple_login():
    correct_username = "admin"
    correct_password = "1234"
    attempts = 0
    while attempts < 3:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == correct_username and password == correct_password:
            print("Welcome!")
            return
        else:
            print("Wrong username or password.")
            attempts += 1
    print("Account locked.")

#TODO: Medium Tasks
#! Task 9: ATM withdrawal
#*A customer's account has 500 AZN. Write a program that repeatedly asks how much they want to 
#*withdraw. The rules: 
#*- If the amount is 0, the program ends and prints "Goodbye". 
#*- If the amount is negative, print "Invalid amount" and ask again. 
#*- If the amount is more than the balance, print "Insufficient funds" and ask again. 
#*- Otherwise subtract it from the balance and print the new balance.

def atm_withdrawal():
    balance = 500
    while True:
        amount = int(input("Enter amount to withdraw (0 to exit): "))
        if amount == 0:
            print("Goodbye")
            break
        elif amount < 0:
            print("Invalid amount")
        elif amount > balance:
            print("Insufficient funds")
        else:
            balance -= amount
            print(f"New balance: {balance}")

#! Task 10: Run the code
#* output: Wrong PIN, 3 attempts left Wrong PIN, 2 attempts left Access granted Attempts used: 2

#! Task 11: Exam results
#* A teacher enters students' exam grades one at a time (0-100). Entering -1 means there are no more 
#* grades. When the input ends, print: how many students passed (grade 51 or above), how many 
#* failed, the highest grade, and the average grade rounded to 1 decimal place. 
#* Do not store the grades anywhere - calculate everything while the grades are being entered. 

def exam_results():
    passed = 0
    failed = 0
    highest_grade = -1
    total_grades = 0
    count = 0

    while True:
        grade = int(input("Enter student's grade (or -1 to finish): "))
        if grade == -1:
            break
        if grade >= 51:
            passed += 1
        else:
            failed += 1
        if grade > highest_grade:
            highest_grade = grade
        total_grades += grade
        count += 1

    average_grade = total_grades / count if count > 0 else 0
    print(f"Students passed: {passed}")
    print(f"Students failed: {failed}")
    print(f"Highest grade: {highest_grade}")
    print(f"Average grade: {average_grade:.1f}")

#! Task 12: Parking garage
#* A garage has 20 parking spaces. The program keeps reading commands from the user: in means a car 
#* enters, out means a car leaves, stop ends the program. After every command print how many spaces 
#* are free. 
#* - If a car tries to enter when the garage is full, print "Garage full" and do not count it. 
#* - If a car tries to leave when the garage is empty, print "Garage is empty". 
#* - Any other word: print "Unknown command". 

def parking_garage():
    totalSpaces = 20
    while True:
        command = input("Enter command (in, out, stop): ")
        if command == "in":
            if totalSpaces > 0:
                totalSpaces -= 1
                print(f"Spaces free: {totalSpaces}")
            else:
                print("Garage full")
        elif command == "out":
            if totalSpaces < 20:
                totalSpaces += 1
                print(f"Spaces free: {totalSpaces}")
            else:
                print("Garage is empty")
        elif command == "stop":
            print("Stopping the program.")
            break
        else:
            print("Unknown command")

#! Task 13: Weather report
#* Ask for the temperature on each of the 7 days of the week. Then print how many days were hot 
#* (above 30 degrees) and which day number was the hottest. 

def weather_report():
    hotDays = 0
    hottestDay = 1
    baseTemperature = int(input("Enter the temperature for day 1:"))
    if baseTemperature > 30:
        hotDays += 1
    dayCount = 2
    while dayCount < 8:
        temperature = int(input(f"Enter the temperature for day {dayCount}:"))
        if temperature > 30:
            hotDays += 1
        if temperature > baseTemperature:
            baseTemperature = temperature
            hottestDay = dayCount
        dayCount += 1

    print(f"There were {hotDays} hot days.")
    print(f"The number of the hottest day was {hottestDay}")

#! Task 14: Find the bug
#* This login program is supposed to lock the account after 3 wrong passwords, but in practice the user 
#* can keep trying forever. Find the mistake, explain it in one sentence, and write the corrected 
#* program. 

#? password = "secret" 
#? while True: 
#?     attempts = 0 
#?     entered = input("Password: ") 
#?     if entered == password: 
#?         print("Welcome") 
#?         break 
#?     attempts += 1 
#?     if attempts == 3: 
#?         print("Account locked") 
#?         break 

#$ The bug is that the attempts variable is inside the loop, so it resets to 0 every time the loop starts.

#! Task 15: Password strength
#* Ask the user for a password and go through it character by character. Count how many digits, 
#* uppercase letters and lowercase letters it has (use .isdigit(), .isupper(), .islower()). The password is 
#* strong if it has at least 8 characters and at least one of each type. Print "Strong password" or "Weak 
#* password", and if it is weak, say what is missing. 

def password_strength():
    password = input("Enter a password: ")
    digit_count = 0
    upper_count = 0
    lower_count = 0

    for char in password:
        if char.isdigit():
            digit_count += 1
        elif char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    if len(password) >= 8 and digit_count > 0 and upper_count > 0 and lower_count > 0:
        print("Strong password")
    else:
        print("Weak password")
        if len(password) < 8:
            print("Password is too short.")
        if digit_count == 0:
            print("Password must contain at least one digit.")
        if upper_count == 0:
            print("Password must contain at least one uppercase letter.")
        if lower_count == 0:
            print("Password must contain at least one lowercase letter.")

#! Task 16: Savings goal
#* Nigar wants to save 1000 AZN for a laptop. In the first month she saves 50 AZN, and every month she 
#* saves 10 AZN more than the previous month (50, 60, 70, ...). Write a program that prints how much 
#* she has after each month and tells her in which month she reaches the goal. 

def savings_goal():
    savings = 0
    month = 1
    monthly_saving = 50

    while savings < 1000:
        savings += monthly_saving
        print(f"After month {month}, Nigar has saved: {savings} AZN")
        if savings >= 1000:
            print(f"Nigar reached her goal in month {month}.")
            break
        monthly_saving += 10
        month += 1

#! Task 17: Read the code
#* output: 105

#? number = 100 
#? while True: 
#?   number += 1 
#?   if number % 7 == 0 and number % 2 == 1: 
#?   break 
#? print(number) 

#$ break is used to stop the program when the first odd number divisible by 7 is found.

#TODO Hard Tasks
#! Task 18: Bank account menu
#* Combine login and a menu into one program. The account PIN is 2580 and the starting balance is 
#* 1000 AZN. 
#* - Step 1 - Login: the user has 3 attempts to enter the PIN. After the third wrong attempt print "Card blocked" and end the program. 
#* - Step 2 - Menu: after a successful login, show the menu below again and again until the user chooses 4.
#* - Option 1 prints the balance. Option 2 asks for an amount and adds it (reject amounts that are 0 
#* or negative). Option 3 asks for an amount and subtracts it (reject amounts that are negative or 
#* larger than the balance). Option 4 prints "Goodbye" and ends. 
#* - Any other option prints "Invalid choice". 

def bank_account_menu():
    pin = "2580"
    balance = 1000
    attempts = 0

    while attempts < 3:
        userPin = input("Enter your PIN: ")
        if userPin == pin:
            print("Login successful.")
            while True:
                print("Menu:")
                print("1. Check balance")
                print("2. Deposit money")
                print("3. Withdraw money")
                print("4. Exit")
                choice = input("Choose an option: ")
                if choice == "1":
                    print(f"Your balance is: {balance} AZN")
                elif choice == "2":
                    amount = int(input("Enter amount to deposit: "))
                    if amount <= 0:
                        print("Invalid amount.")
                    else:
                        balance += amount
                        print(f"New balance: {balance} AZN")
                elif choice == "3":
                    amount = int(input("Enter amount to withdraw: "))
                    if amount <= 0:
                        print("Invalid amount.")
                    elif amount > balance:
                        print("Insufficient funds.")
                    else:
                        balance -= amount
                        print(f"New balance: {balance} AZN")
                elif choice == "4":
                    print("Goodbye")
                    break
                else:
                    print("Invalid choice.")
        else:
            attempts += 1
            print(f"Wrong PIN, {3 - attempts} attempts left.")

#! Task 19: Vending Machine
#* A bottle of water costs 1.50 AZN. The machine accepts only these coins: 0.05, 0.10, 0.20, 0.50 and 1. 
#* Keep asking the user to insert a coin until the total inserted is 1.50 or more. If the user inserts a coin 
#* that the machine does not accept, print "Coin not accepted" and do not add it. When there is 
#* enough money, print "Here is your water" and, if needed, the change. 
#* Tip: compare floats carefully - use round(total, 2) when printing. 
#* Dont use lists

    def vending_machine():
        total = 0.0
        price = 1.50

        while total < price:
            coin = float(input("Insert a coin (0.05, 0.10, 0.20, 0.50, 1): "))
            if coin == 0.05 or coin == 0.10 or coin == 0.20 or coin == 0.50 or coin == 1:
                total += coin
                print(f"Total inserted: {round(total, 2)} AZN")
            else:
                print("Coin not accepted")
        print("Here is your water")
        if total > price:
            change = round(total - price, 2)
            print(f"Your change is: {change} AZN")
        
#! Task 20: Door codes
#* A security company only allows door codes that are prime numbers between 2 and 100. Write a 
#* program that prints every allowed code on one line, separated by spaces. Then print how many 
#* codes there are. 
#* Remember: a prime number has no divisors other than 1 and itself. You will need a loop inside a 
#* loop. 

def door_codes():
    prime_codes = ""
    count = 0
    for num in range(2, 101):
        for i in range(2, num):
            if num % i == 0:
                break
            else:
                prime_codes += str(num) + " "
                count += 1
                break
    print(prime_codes.strip())
    print(f"Total prime codes: {count}")

#! Task 21: Read the code
#? for floor in range(1, 4): 
#?    for room in range(1, 5): 
#?       if room == 3: 
#?           break 
#? print(floor * 100 + room, end=" ") 
#? print() 

#* output: 101 201 301

#! Task 22: Hotel room list
#* A hotel has 5 floors with 4 rooms on each floor. Room numbers are made from the floor and the 
#* room, so floor 2 has rooms 201, 202, 203, 204. Because of superstition the hotel skips floor 4 
#* completely - it goes 1, 2, 3, 5. Using nested loops, print the room numbers floor by floor, one floor 
#* per line, with the floor number at the start. 

def hotel_room_list():
    for floor in range(1, 6):
        if floor == 4:
            continue
        print(f"Floor {floor}: ", end="")
        for room in range(1, 5):
            print(f"{floor}0{room}", end=" ")
        print() 

#! Task 23: Bank queue
#* A bank teller works 480 minutes a day. Customers are served one after another, and the program 
#* asks how many minutes each customer needs (entering 0 means the queue is empty). Keep serving 
#* customers while there is time left. If the next customer needs more time than is left in the day, print 
#* "Sorry, come back tomorrow" and stop. At the end print how many customers were served and how 
#* many minutes were left. 

def bank_queue():
    total_time = 480
    customers_served = 0

    while total_time > 0:
        customer_time = int(input("Enter the time needed for the next customer (0 to finish): "))
        if customer_time == 0:
            break
        if customer_time > total_time:
            print("Sorry, come back tomorrow")
            break
        total_time -= customer_time
        customers_served += 1

    print(f"Customers served: {customers_served}")
    print(f"Minutes left: {total_time}")

#! Task 24: Vote counting
#* In a class election there are three candidates: A, B and C. The program reads votes one at a time until 
#* the user types end. Each vote must be exactly A, B or C - anything else counts as a spoiled vote. 
#* When the voting ends, print the number of votes for each candidate, the number of spoiled votes, 
#* and the winner. If two or more candidates have the same highest number of votes, print "Tie" 
#* instead of a winner. 

def vote_counting():
    voteA = 0
    voteB = 0
    voteC = 0
    spoiledVotes = 0

    while True:
        vote = input("Please enter your vote (A-B-C, write \"end\" to stop the program):")
        if vote == "A":
            voteA += 1
        elif vote == "B":
            voteB += 1
        elif vote == "C":
            voteC += 1
        elif vote == "end":
            break
        else:
            spoiledVotes += 1

    print(f"The number of votes for candidate A: {voteA}")
    print(f"The number of votes for candidate B: {voteB}")
    print(f"The number of votes for candidate C: {voteC}")
    print(f"The number of spoiled votes: {spoiledVotes}")
    if voteA == voteB == voteC:
        print("All three candidates tied")
    elif voteA == voteB and voteA > voteC:
        print("A and B are tied")
    elif voteA == voteC and voteA > voteB:
        print("A and C are tied")
    elif voteB == voteC and voteB > voteA:
        print("B and C are tied")
    elif voteA > voteB and voteA > voteC:
        print("A is the winner")
    elif voteB > voteA and voteB > voteC:
        print("B is the winner")
    else:
        print("C is the winner")

#! Task 25: Card number check
#* Banks check whether a card number was typed correctly using the Luhn algorithm. Ask the user for a 
#* 16-digit card number (as a string, no spaces) and check it like this: 
#* - Go through the digits from right to left. 
#* - Every second digit (the 2nd, 4th, 6th ... counting from the right) is doubled. If the doubled value is bigger than 9, subtract 9 from it. 
#* - Add up all the digits (the doubled ones and the untouched ones). 
#* - If the total is divisible by 10, the number is valid. 
#* Print "Valid card number" or "Invalid card number". If the input is not exactly 16 digits, print "Must 
#* be 16 digits" and ask again. 

def card_number_check():
    while True:
        cardNumber = input("Enter a 16-digit card number: ")
        if len(cardNumber) != 16 or not cardNumber.isdigit():
            print("Must be 16 digits")
            continue
        cardNumber = list(cardNumber)
        for i in range(0, len(cardNumber), 2):
            digit = int(cardNumber[i])
            digit *= 2
            if digit > 9:
                digit -= 9
            cardNumber[i] = str(digit)
        sum = 0
        for i in range(0, len(cardNumber)):
            sum += int(cardNumber[i])
        if sum % 10 == 0:
            print("Valid card number")
        else:
            print("Invalid card number")

