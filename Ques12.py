#Write a python program that calculates the sum of the digits of a given number

def digits_sum(a):
    sum=0
    while a>0:
        b=a%10
        a=a//10
        sum+=b
    print(sum)

digits_sum(88)