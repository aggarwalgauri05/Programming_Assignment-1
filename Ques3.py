#Write a python program that calculates the factorial of a given number

def factorial(a):
    fact=1
    for i in range(2,a+1):
        fact*=i
    print(fact)

factorial(77)