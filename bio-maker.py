# new line = \n 
import time

a = input("type your name here: ") # my name is ___
a = str(a)
b= input("type your age here: ") # my age is ___
b = str(b)
c =  input("type what you are doing currently: ") # i am ___
c = str(c)
time.sleep(1)
d = f'''
Name: {a}\n
Age: {b}\n
Currently: {c}\n
'''
print(d)
    #prints your bio with a new line
time.sleep(0.5)
print("is this fine?")
t = input("confirm your answer: ")
if t == "yes":
    print("Your inputs have been taken successfully.")
    with open(f"inputs/{a}_input.txt", "w") as f:
        f.write(d) 
else:
    print("please re-enter your inputs.")
time.sleep(0.5)
print("Thanks For Using Me UwU\n Coded By Aero With Love")
time.sleep(5)
print("END")