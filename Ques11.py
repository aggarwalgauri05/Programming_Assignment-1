#Write a python program that generates the first n numbers in the Fibonacci sequence

def fibb(n):
    a=0
    b=1
    print(a)
    for i in range(n-1):
        print(b)
        temp=a
        a=b
        b= b+temp
fibb(60)