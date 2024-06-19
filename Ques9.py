#Write a python program that checks if a substring is present in a given string

def substr(a,b):
    if b in a:
        print("YES")
    else:
        print("NO")

substr('I live in India','in')