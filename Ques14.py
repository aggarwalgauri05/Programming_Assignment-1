#Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.

content=[]
while True:
    a=input()
    if a:
        content.append(a)
    else:
        break
for i in content:
    print(i)