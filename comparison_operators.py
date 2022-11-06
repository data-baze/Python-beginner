can_code = True

if can_code == True:
    #do a thing 
    print("you can code!")
else:
    #do something else
    print("you don't know how to code yet")
student = "Data Bassey"

if student == "Data Bassey":
    print("show students portal")

else:
    print("you are a student, Welcome to Python 101")


name = input("What is your name?")
if name == "Data":
    print("welcome Data!")
    bring_food = "Pizza"
elif name == "Bob":
    print("Welcome to your teacher portal")
    bring_food = "Tacos"
else:
    print("you're not Data get outta here")
    bring_food = "Salmon"

print(f"You are eating {bring_food}")