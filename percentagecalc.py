import time

oplist = ('''Here You can \n1. Convert a decimal into a percentage. \n2. Convert a percentage into a decimal. \n3. Take out percentage''')

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

print("Welcome to percentage calculator")
print(oplist)

i = input("what operation do you want to perform? \n")
i = int(i)

if i == 1:
    c = input("Enter the decimal amount: \n")
    c = float(c)
    
    dcml = (c*100)
    print("evaluating values....")
    time.sleep(2)
    print("printing the percentage...")
    print(dcml)

if i == 2:
    d = input('''Enter the percentage amount: \n''') # without '%' sign
    d = float(d)
    e = (d/100)
    print("evaluating values....")
    time.sleep(2)
    print("printing the decimal...")
    print(e)

if i == 3:
    a = input("Enter the total amount: \n")
    a = int(a)

    b =  input("Enter the amount gained: \n")
    b = int(b)

    prcnt = (b/a)*100
    print("evaluating values....")
    time.sleep(2)
    print("printing the percentage...")
    print(prcnt)
  
time.sleep(1)
  
if i == 1 or 2 or 3:
    print("thanks for using the percentage calculator. \n❤️")
    
# this program ends here 