import time



# poem = open('poems.txt')
# twinkle = poem.read()
# if 'twinkle' in twinkle:
#     print("the word twinkle is present")

#     time.sleep(0.5)

# else:
#     print("the word twinkle isn't present")

# poem.close()




# def game():
#     return 64

# score = game()

# with open('hiscore.txt') as f:
#    hiscore = f.read()
   
      
#    if hiscore=='':
#        with open('hiscore.txt', 'w') as f:
#            f.write(str(score))

#    elif int(hiscore)<score or hiscore=='':
#        with open('hiscore.txt', 'w') as f:
#            f.write(str(score))




# print("Welcome To Table Generator")
# print("This Generator Generates In Ranges")
# a = int(input("Enter The First Number\n"))
# b = int(input("Enter The Second Number\n"))
# time.sleep(1)
# print(f"You'll Get 10 Multiples Of {a}, {b}")
# time.sleep(0.5)
# print("Generating Tables.....")




# for i in range(a, b):
#     with open(f"tables/Multiplication_Table_Of_{i}.txt", "w") as f:
#         for j in range(1, 11):
#             f.write(f"{i}x{j}={i*j}\n")
#             if j!=10:
#                 f.write('\n')
                
# print("Generation Was Successfull")
# # creates .txt files in a folder with specified name and writes the multiplication tables in it









print("file preview...")
with open('cat.txt', 'r') as f:
    p = f.read()
    print(p)
find = input("Enter What Word Should Be Selected\n")
replace = input(f"Enter What Word Should {find} Be Replaced With\n")
with open('cat.txt', 'r') as f:
    c = f.read()
    c = c.replace(find, replace)                

with open('cat.txt', 'w') as f:
    f.write(c)  
print("Printing cat.txt Here... ")
time.sleep(0.5)
with open('cat.txt', 'r') as f:
    o = f.read()
    print(o)

print("The Required Edits Are Successfully Recorded")

# ends here
