print("welcome")

#making the seperation lines

line = "==============================="

def new_line():
    print(line) 

#these lines will be used to seperate sections

# =============================== gather name info and age ===============================

new_line()

# making a while loop to see if the user doesnt leave it blank

fn = "" # -- first name = fn
while fn == "":
    fn = input("What is your first name? ")
    # check for valid input, if good then break the loop
    if fn != "": break
    else: fn = input("What is your first name? ")
fn.lower()

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

print(f"welcome {fn}.")
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



#asking user waht choice they want

def Get_camp():
    while True:
        try:
            Ask1 = int(input("Please select a number for what camp you want: "))
            if Ask1 > 0 or Ask1 < 4:
                return Ask1
            else: print("Your choice must be 1-3 please Enter again")
        except ValueError:
            print("That's not a valid number!")



#printing camp options

Camp_list()
Get_camp()

new_line()

# asking user what meal they want

def Get_meal():
    while True:
        try:
            Ask2 = int(input("Please select a number for what meal you want: "))
            if Ask2 > 0 or Ask2 < 4:
               return Ask2
            else: print("Your choice must be 1-3 please Enter again")
        except ValueError:
           print("That's not a valid number!") #making sure they put a number

# printing meal options

meal_list()
Get_meal()

#turning the tuples into variables

ask1 = (Get_camp)
ask2 = Get_meal

new_line()

# =============================== concluding everything =============================== 

print(f'{fn}, age {age}, has chosen {campList[ask1 - 1]}, alongside a meal option of: {mealList[ask2 - 1]}')
print(f"This camp will last {dayList[ask1 - 1]}, It's considered {dificultyList[ask1 - 1]} and an additional cost of {costList[ask1 - 1]}")
