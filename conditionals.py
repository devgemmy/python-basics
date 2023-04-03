# if and else 
a = 5
age = 18
ageMax = 45

if (a < age):
    print("You are too young to join the club")
    print("Wait, " + str(age - a) + " more years")
elif (a > age and a < ageMax):
    print("Welcome to the club!!")
elif (a > ageMax):
    print("You are to old to join the club!!")


# print(a) if a < age else print(age)

# while
basket = 3
while basket <= 10:
    print(basket)
    basket += 1

# for
objects = ['umbrella', 'pen', 'book']

for x in objects:
    if (x == 'pen'):
        continue
    print(x)
    