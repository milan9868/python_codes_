import time

print("Welcome To Akshats'-Certificate-Of-Chad-Education")

# # data/info ladder
examtype = str(input("Which Exams' Report Card Do You Want?\n")) # terminal, annual, monthly, weekly, etc
name = str(input("Enter Your Full-Name\n")) # Akshat Singh Kushwaha, akshat singh kushwaha, AKSHAT SINGH KUSHWAHA


time.sleep(2)




# grades table
grades = '''
A+ = 90+
B = 80
F = Below 80
Below 80 = F 
*because you are an Indian and getting below 0 is a sin*
'''

# input ladder 
a = int(input("Enter Your Marks In English\n"))
b = int(input("Enter Your Marks In Hindi\n"))
c = int(input("Enter Your Marks In Science\n"))
d = int(input("Enter Your Marks in Social Studies\n"))
e = int(input("Enter Your Marks In Sanskrit\n"))




# arithmetical table
marks = [a, b, c, d, e]
full = a+b+c+d+e
merks = full/5
print(f"You've Scored {merks}% in {examtype}")





time.sleep(2)
print("Grade Table")
print("You'll Be Given A Grade According To Your Scores")
time.sleep(1)
print(grades)





# grading systems' if else ladder
'''
A+ = 90+
B+ = 80+
F = Below 80
Below 80 = F because you are an Indian and getting below 0 is a sin
'''

if merks <= 80:
    print("You've Got Grade F")

elif merks >= 90:
    print("You've Got Grade A+")
    
elif merks <= 89:
    print("You've Got Grade B+")

time.sleep(1)




card = f'''
┇-------------------------ᴀᴋꜱʜᴀᴛꜱ' ᴄᴇʀᴛɪꜰɪᴄᴀᴛᴇ ᴏꜰ ᴄʜᴀᴅ ᴇᴅᴜᴄᴀᴛɪᴏɴ--------------------------                     
┇{examtype} Exams' Report Card  
┇┝Students' Name = {name}                                                               
┇┝Scores = {merks}   
┇                                                         
┇                                                                                        
┇----------ᴍᴀʀᴋꜱ----------                                                               
┇┝English - {a}          ┇                                                               
┇┝Hindi - {b}            ┇
┇┝Science - {c}          ┇
┇┝Social Studies - {d}   ┇
┇┝Sanskrit - {e}         ┇
┇┝ Total = {full}/500    ┇
┇-------------------------
┇Banned Mathematics lmfao 💪
┇
┇
┇Chad Education 💪
┇----------------------------------------------------------------------------------------
'''

print("Printing Your Report Card")
print(card)
print("Thank You For Using This Program To Calculate You ACCE Board Exams' Scores")




























































# if (sum(marks))<=165:
#     print("You haven't failed in any of the subjects and you'll be given a grade")
#     print("Getting Grades Table")
#     # time.sleep(5)    
#     print(grades)


# Unused Arguments



# # if a <= 33:
#     print(f"You've Failed In English")
    
# if b <= 33:
#     print(f"You've Failed In Hindi")

# if c <= 33:
#     print(f"You've Failed In Science")

# if d <= 33:
#     print(f"You've Failed In Social Studies")

# if e <= 33:
#     print(f"You've Failed In Sanskrit")
# unused arguments




# print("Getting Grades Table")
# time.sleep(5)    
# print(grades)
 