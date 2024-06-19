#Write a program that takes a string input from the user and writes it to a text file 

str = input("Enter your text")
with open ('new.txt','w') as x:
    x.write(str)