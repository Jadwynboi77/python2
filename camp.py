print("welcome")
# ------ gather name info and age
# making a while loop to see if the user doesnt leave it blank
fn = "" # -- first name = fn
while fn == "":
    fn = input("What is your first name? ")
    # check for valid input, if good then break the loop
    if fn != "": break
    else: fn = input("What is your first name? ")
fn.lower()

# asking and testing if age is 5-17
try:
    Age = int(input("Please enter your age: "))
    if Age < 5:
        print("Sorry, you are too young.")
        exit()
    elif Age > 17:
        print("Sorry, you are too old.")
        exit()
# if there is an exception, print this out
except ValueError:
  print("That's not a valid number!")

# -- informing the user

print(f"welcome {fn}.")
print("you will now be given a choice of Camps")

# --- making the lists
campList = ["Cultural immersion","Kayaking and pancakes","Mountain biking"]
mealList = ["standered","vegetarain","dairy-free"]
dayList = [5,3,4]
costList = [800,400,900]
dificultyList = ["easy","moderite","difficult"]
count = 0
#the bypass allows this list to start at 1, instead of starting at 0

#creating the defines (tuples)
def Camp_list():
    print(f'1. {campList[count]}, included with a fee of {costList[count]} and is considered "{dificultyList[count]}".')
    print(f'2. {campList[count + 1]}, included with a fee of {costList[count + 1]} and is considered "{dificultyList[count + 1]}".')
    print(f'3. {campList[count + 2]}, included with a fee of {costList[count + 2]} and is considered "{dificultyList[count + 2]}".')

def meal_list():
    print(f'1. {mealList[count]}')
    print(f'2. {mealList[count + 1]}')
    print(f'3. {mealList[count + 1]}')