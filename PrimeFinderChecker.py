import math

def IsPrime(num):
    if num == 2 or num == 3: 
        return True
    if num < 2 or num % 2 == 0: 
        return False
    if num < 9: 
        return True
    if num % 3 == 0: 
        return False
    root = int(math.sqrt(num))
    mult = 5 # primes are of the form 6n+-1
    while mult <= root:
        if num % mult == 0: return False # 6n-1 checker
        if num % (mult + 2) == 0: return False # 6n+1 checker
        mult += 6
    return True

choice = int(input("Finder(1) or Checker(2): "))
if choice == 1:
    number = 1
    while True:
        if IsPrime(number) == True:
            print(number)
        number += 1
elif choice == 2:
    number = int(input("Enter number to check: "))
    if IsPrime(number) == True:
        print("True")
    else:
        print("False")
else:
    print("Invalid input")