print("welcome")

#making the seperation lines

line = "==============================="

def new_line():
    print(line) 

#these lines will be used to seperate sections

# =============================== gather name info and age ===============================
# =============================== name info ===============================

new_line()

# making a while loop to see if the user doesnt leave it blank

Campers_name = ""
while Campers_name == "":
    Campers_name = input("What is your first name? ")
    # check for valid input, if good then break the loop
    if Campers_name != "": break
    else: Campers_name = input("What is your first name? ")
Campers_name.lower()

# =============================== age info ===============================

# asking and testing if age is 5-17
min_age = 5 #the names should explain it
max_age = 17

def Get_age():
    while True:
        try:
            Age = int(input("Please enter your age: "))
            if Age > 0: #to make sure its not a negitave number 
                return Age
            else: print("Age cannot be 0 or include symbols, please Enter again")
        except ValueError: #to make sure it is a number 
            print("That's not a valid number!") 
            

age = Get_age()

# =============================== leader Option ===============================

def Leader(): #if the age is 15-17, they can have the choice to be a leader
    while True:
        try:
            if age >= 15: 
                print("Because you are over the age of 15") #telling them why they have the option
                AskLeader = input("Would you like to volunteer for camp leader? (yes/no): ")
                AskLeader.lower #making it all lowercase
                if AskLeader == "yes":
                    AskLeader = True
                    return AskLeader
                elif AskLeader == "no":
                    AskLeader = False
                    return AskLeader
                else: 
                    print("Thats not a valid awnser!")
        except ValueError: #to make sure it is a number
            print("That's not a valid number!") 

def Age_validation():
    while True:
        if age < min_age: # minimum age
            print("Sorry, you are too young.")
            exit()
        elif age > max_age: # maximum age
            print("Sorry, you are too old.")
            exit()
        else: print(f"welcome {Campers_name}.")
        break

Age_validation()

# -- informing the user

new_line()
if age >= 15:
    leaderconfirm = Leader() #making the function into a value




print("you will now be given a choice of Camps")

# =============================== making the lists ===============================

campList = ["Cultural immersion","Kayaking and pancakes","Mountain biking"] #list for the camp choice
mealList = ["standered","vegetarain","dairy-free"] #list for the meals
dayList = [5,3,4] # list for the amount of days
costList = [800,400,900] #list for the cost
dificultyList = ["easy","moderite","difficult"] #list for how difficult it will be
count = 0 #will be used to tally up what number of the list will be chosen for output

#creating the defines (tuples)

def Camp_list():
    print(f'1. {campList[count]}, included with a fee of {costList[count]} and is considered "{dificultyList[count]}".')
    print(f'2. {campList[count + 1]}, included with a fee of {costList[count + 1]} and is considered "{dificultyList[count + 1]}".')
    print(f'3. {campList[count + 2]}, included with a fee of {costList[count + 2]} and is considered "{dificultyList[count + 2]}".')

def meal_list():
    print(f'1. {mealList[count]}')
    print(f'2. {mealList[count + 1]}')
    print(f'3. {mealList[count + 2]}')

# =============================== printing list ===============================
# =============================== camp list =============================== 

new_line()

Camp_list()

#asking user waht choice they want

def Get_camp():
    while True:
        try:
            question1 = int(input("Please select a number for what camp you want: "))
            if question1 == 1:
                question1 - 1
                return question1
            elif question1 == 2:
                question1 - 1
                return question1
            elif question1 == 3:
                question1 - 1
                return question1
            else: print("Your choice must be 1-3 please Enter again")
        except ValueError:
            print("That's not a valid number!")

#turning the camp tuples into variables
#Question1 is now a variable that can be used with a f string (Diference being capital Q)
#qustion1 remains a function, and can not be used in a f string (Diference being Lowercase Q)
Question1 = Get_camp()

new_line()
# =============================== meal list ===============================

# asking user what meal they want

def Get_meal():
    while True:
        try:
            question2 = int(input("Please select a number for what meal you want: "))
            if question2 > 0 or question2 < 4:
               return question2
            else: print("Your choice must be 1-3 please Enter again")
        except ValueError:
           print("That's not a valid number!") #making sure they put a number


#turning the meal tuples into variables

meal_list()
Question2 = Get_meal()

# printing meal options

new_line()
# =============================== shuttle option =============================== 

shuttleChoice = 0 #for the output
ShuttleList = ["No","Yes"]

def Shuttle():
    while True:
        try:
            question3 = input("would you like to take a shuttle transport? (Yes or no): ")
            if question3.lower() == "yes" or question3.lower() == "no":
               return question3
            else: print("Your choice must Yes or No please Enter again")
        except ValueError:
           print("Awnser cannot be a number!") # making sure they don't put a number

Question3 = Shuttle()

cost = costList[Question1 - 1] # presetting the cost so if they say no its still gonna run the {cost} in the output

if Question3 == "yes":
    shuttleChoice = 1
    cost += 80 # cost of transport

# =============================== concluding everything =============================== 

new_line()

print(f"Name: {Campers_name}")
print(f"Age: {age}")
print(f"camp selection: {campList[Question1]}")
print(f"Days: {dayList[Question1]}")
print(f"Difficulty: {dificultyList[Question1]}")
print(f"Meal: {mealList[Question2 - 1]}")
print(f"Shuttle: {dificultyList[shuttleChoice]}")

# =============================== confirm everything =============================== 

def Confirm():
    while True:   
        Final_question = input("would yopu like to confirm? (Yes or no): ")
        if Final_question.lower() == "yes" or Final_question.lower() == "no":
           return Final_question
        else: print("Your choice must Yes or No please Enter again")

final_Question = Confirm()

if final_Question == "yes": print("Great, we can't wait to see you there! :) ")
elif final_Question == "no":
    print(f"{Campers_name} has not confirmed")
    exit()