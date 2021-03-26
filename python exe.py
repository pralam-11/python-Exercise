def getdate():
    import datetime
    return datetime.datetime.now()
def intake(n):
    if n == 1:
        save = int(input("Enter 1 for food and 2 for exercise"))
        if save == 1:
            val = input("Enter hare: ")
            with open("Breakfast-fo.txt", "a") as f:
                date = ("[", getdate(), "]")
                f.write(f"{date}, {val}""\n")
                print("succesfully added")


        else:
            val = input("Enter here: ")
            with open("Morning-exe.txt", "a") as s:
                date = ("[", getdate(), "]")
                s.write(f"{date}, {val}""\n")
                print("succesfully added")

    elif n == 2:
        save = int(input("Enter 1 for food and 2 for exercise"))
        if save == 1:

            val = input("Enter hare: ")
            with open("Lunch-fo.txt", "a") as op:
                date = ("[", getdate(), "]")
                op.write(f"{date}, {val}""\n")
                print("succesfully added")

        else:
            val = input("Enter hare: ")
            with open("Afternoon-exe.txt", "a") as d:
                date = ("[", getdate(), "]")
                d.write(f"{date}, {val}""\n")
                print("succesfully added")


    else:
        save = int(input("Enter 1 for food and 2 for exercise"))
        if save == 1:
            val = input("Enter hare: ")
            with open("Dinner-fo.txt", "a") as op:
                date = ("[", getdate(), "]")
                op.write(f"{date}, {val}""\n")
                print("succesfully added")

        else:
            val = input("Enter hare: ")
            with open("Evening-exe.txt", "a") as d:
                date = ("[", getdate(), "]")
                d.write(f"{date}, {val}""\n")
                print("succesfully added")

def retrive(j):
    if j == 1:
        save = int(input("Enter 1 for food and 2 for exercise"))
        if save == 1:
            with open("Breakfast-fo.txt") as d:
                for i in d:
                    print(i, end="")
        else:
            with open("Morning-exe.txt") as t:
                for i in t:
                    print(i,end="")
    elif j == 2:
        save = int(input("Enter 1 for food and 2 for exercise"))
        if save == 1:
            with open("Lunch-fo.txt") as d1:
                for i in d1:
                    print(i, end="")
        else:
            with open("Afternoon-exe.txt") as t1:
                for i in t1:
                    print(i, end="")
    else:
        save = int(input("Enter 1 for food and 2 for exercise"))
        if save == 1:
            with open("Dinner-fo.txt") as d2:
                for i in d2:
                    print(i, end="")
        else:
            with open("Evening-exe.txt") as t2:
                for i in t2:
                    print(i, end="")


print("\n")
print("    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ")
print("    Welcome To Healtcare Management   ")
print("    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   ")

a = int(input("1 to log and 2 to retrive"))

if a == 1:
    b = int(input("Enter 1 for Breakfast or Exercise\nEnter 2 for Lunch or Exercise\nEnter 3 for Dinner or Exercise:"))
    intake(b)

else:
   b = int(input("Enter 1 for Breakfast Diet or Morning Erercise\nEnter 2 for Lunch Died or Afternoon Exercise\nEnter 3 for Dinner Diet or Evening erercise:"))
   retrive(b)

