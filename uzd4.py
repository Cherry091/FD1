import random
number = random.randint(1, 10)
minējums = int(input("Uzmini skaitli no 1-10"))
while minējums != number: 
    if minējums > number:
        print ("Par lielu")
    elif minējums < number:
        print ("Par mazu")
    number = random.randint(1, 10)
if minējums == number:
        print("Pareizs minējums")
        
        
