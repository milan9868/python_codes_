# # practice set
# # highest value calculator [3]

import time
# print("Welcome to highest value caculator [3]")
# time.sleep(1)


# def maximum(num1, num2, num3):
#     if (num1>num2):
#         if (num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if (num2>num3):
#             return num2
#         else:
#             return num3      
# a = int(input("Enter The First Number\n"))
# b = int(input("Enter The Second Number\n"))
# c = int(input("Enter The Third Number\n"))
# max = maximum(a,b,c)
# print(f"The maximum value in {a}, {b} & {c} is {max}")



# celsius to farenheit converter

# print("Welcome To Celsuis To Farenheit")
# time.sleep(1)

# def farh(cel):
#     return (cel*(9/5)) + 32 


# c = int(input("Enter The Celsuis Temperature\n"))
# fdegree = farh(c)
# print(f"The Temperature {c}°C in Farenheit Is {fdegree}°F")



# # preventing python print function from printing a new line

# print("Hello", end=" ")
# print("World", end=" ")



# n = int(input("Enter A Number\n"))
# for i in range(n):
#     print("*"*(n-i))
    
    
# # ***
# # **
# # *
# # prints this sort of pattern ^^
    
# def i2cm(k):
#     return (k*2.54)

# k = int(input("Input Lenght In Inches\n"))
# sed = i2cm(k)
# print(f"The Lenght of {k}inches in centimeters is {sed}")
    
  
  
  
# # converts length in inches into lenght in centimeters ^^  


# strip cmd
def remove_and_strip(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

# # --------------------------------------------------------------------------------------------------------------------

st = str(input("Type A Sentence\n"))
rem = str(input("Input The Words You Want To Get Stripped\n"))
sedge = remove_and_strip(st, rem)
print(sedge)

# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------













