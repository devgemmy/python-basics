def happy_birthday(name, age):
    print(f"{name}, Happy birthday!")
    print(f"Are you {age} years old?")
    
happy_birthday("Kevin", "9")


def registerStudent(name, age, gender, grade):
    student = {
        "p_name": name,
        "p_age": age,
        "p_gender": gender,
        "p_grade": grade
    }

    print(student["p_name"])

# exp_name = input("Enter your name: ")
# exp_age = input("Enter your age: ")
# exp_gender = input("Are you male or female? ")
# exp_grade = input("What class are you in? ")   

# registerStudent(exp_name, exp_age, exp_gender, exp_gender)


add = lambda x, y : x + y
print(add(78, 90))


def multiplier(a):
    return lambda n: a * n

doubling = multiplier(2)
tripling = multiplier(3)
print(tripling(11))

# CONSTRUCTOR FUNCTION 