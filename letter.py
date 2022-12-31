import time

ltr = '''Dear, <|n|>
You've Been asked to attend a meeting on the weekend

Date: <|d|>
'''

n = input("Enter Name\n")
d = input("Enter Date\n")

ltr = ltr.replace("<|n|>", n)
ltr = ltr.replace("<|d|>", d)
print("writing letter with the changed inputs................................................................")
time.sleep(2)
print(ltr)

# prints the ltr with changed name and date