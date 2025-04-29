print("welcome")
# ------ gather name info and age
#making a while loop to see if the user doesnt leave it blank
fn = "" # -- first name = fn
while fn == "":
    fn = input("What is your first name? ")
    #check for valid input, if good then break the loop
    if fn != "": break
    else: fn = input("What is your first name? ")