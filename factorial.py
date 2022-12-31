# factorial calculator 

# n! = 1*2*3*4*5*6*7*8.....*n

# n = int(input("Enter The Number Of Factorial Factors You Want\n"))
# p = int(input("Enter The Number Of Which You Want Factorial Of\n"))
# for i in range(n):
#     p = p*(i+1)
# print(p)
# just a program --




# def factorial_iterative(n):

#     n = int(input("Enter The Number Of Factorial Factors You Want\n"))
#     p = int(input("Enter The Number Of Which You Want Factorial Of\n"))

# #----------------------------------------------------------------------
#     for i in range(n):
#          p = p * (i+1)
#     return p



# # function ends here

# # calling the function 📞
# print(factorial_iterative(5))





def factorial_recursive(a):
    if a == 1 or a == 0: # base condition which doesn't call the function anymore
        return 1
    return a * factorial_recursive(a-1) # function calling itself
abc = int(input("Enter the number of which you want a factorial of\n"))
fc = factorial_recursive(abc)
print(f"The Factorial of {abc} is\n {fc}")


# printing factorial using recursive method


