print("welcome")

#making the seperation lines

line = "==============================="

def new_line():
    print(line) 

#these lines will be used to seperate sections

# =============================== gather name info and age ===============================

new_line()

# making a while loop to see if the user doesnt leave it blank

Campers_name = ""
while Campers_name == "":
    Campers_name = input("What is your first name? ")
    # check for valid input, if good then break the loop
    if Campers_name != "": break
    else: Campers_name = input("What is your first name? ")
Campers_name.lower()

# asking and testing if age is 5-17
def Get_age():
    while True:
        try:
            Age = int(input("Please enter your age: "))
            if Age > 0:
                return Age
            else: print("Age cant be negitive, please Enter again")
        except ValueError:
            print("That's not a valid number!")
            

age = Get_age()

def Age_validation():
    while True:
        if age < 5:
            print("Sorry, you are too young.")
            return age
        elif age > 17:
            print("Sorry, you are too old.")
            return age

new_line()

# -- informing the user

print(f"welcome {Campers_name}.")
print("you will now be given a choice of Camps")

# =============================== making the lists ===============================

campList = ["Cultural immersion","Kayaking and pancakes","Mountain biking"]
mealList = ["standered","vegetarain","dairy-free"]
dayList = [5,3,4]
costList = [800,400,900]
dificultyList = ["easy","moderite","difficult"]
count = 0
meal = True

#creating the defines (tuples)

def Camp_list():
    print(f'1. {campList[count]}, included with a fee of {costList[count]} and is considered "{dificultyList[count]}".')
    print(f'2. {campList[count + 1]}, included with a fee of {costList[count + 1]} and is considered "{dificultyList[count + 1]}".')
    print(f'3. {campList[count + 2]}, included with a fee of {costList[count + 2]} and is considered "{dificultyList[count + 2]}".')

def meal_list():
    print(f'1. {mealList[count]}')
    print(f'2. {mealList[count + 1]}')
    print(f'3. {mealList[count + 1]}')

# =============================== printing list ===============================

new_line()

Camp_list()

#asking user waht choice they want

def Get_camp():
    while True:
        try:
            question1 = int(input("Please select a number for what camp you want: "))
            if question1 > 0 or question1 < 4: #meal choice is only 1-3
                return question1
            else: print("Your choice must be 1-3 please Enter again")
        except ValueError:
            print("That's not a valid number!")

#turning the camp tuples into variables
question1 = Get_camp


#printing camp options


Get_camp()

new_line()

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
question2 = Get_meal

# printing meal options

meal_list()
Get_meal()

new_line()

# =============================== concluding everything =============================== 

print(f'{Campers_name}, age {age}, has chosen {campList[question1]}, alongside a meal option of: {mealList[question2]}')
#print(f"This camp will last {dayList[question1 - 1]}, It's considered {dificultyList[question1 - 1]} and an additional cost of {costList[question1 - 1]}")
