# class Number:
#     def sum(self):
#         return self.a +self.b  # type: ignore

# num = Number()
# num.a = int(input("Enter A Number\n"))
# num.b = int(input("Enter Another Number\n"))
# s = num.sum()
# print(f"The sum of the above numbers is {s}")
# # oop project 1




# class RailwayForm:
#     type = "RailwayForm"
#     def printData(self):
#         print(f"Passengers' Name\n {self.name}")
#         print(f"Passengers' Train\n {self.train}")
#         print(f"Passengers' Beginning Of Journey\n {self.beginning}")
#         print(f"Passengers' Destination Of Journey\n {self.destination}")
 
 
    
# akshatsApplication = RailwayForm()
# akshatsApplication.name = "Akshat"
# akshatsApplication.train = "Rajdhani Express"
# akshatsApplication.destination = "Kolkata, West Bengal, India"
# akshatsApplication.beginning = "New Delhi, India"
# akshatsApplication.printData() # oop project 2




# class Staff: 
#     workspace = "Graphics Code"
#     salary = 10000
    
#     def __init__(self, age, country, name):
#         self.age = age
#         self.country = country
#         self.name = name
#         print(f'''Staff Details:
# Name: {self.name}
# Age: {self.age} 
# Country: {self.country}
#               ''')
    
# aero = Staff("Akshat Singh",15, "India")
    
# gatik = Staff()
# adnan = Staff()
# wadhwa = Staff()

# gatik.salary = 5000
# wadhwa.salary = 40000
# print(f"{Staff.workspace}'s Staffs Salary List")
# print(f"Salary Of Gatik Is {gatik.salary} Per Month\n Per Annum = {gatik.salary*12}")
# print(f"Salary Of Adnan Is {adnan.salary} Per Month\n Per Annum = {adnan.salary*12}")
# print(f"Salary Of Wadhwa Is {wadhwa.salary} Per Month\n Per Annum = {wadhwa.salary*12}")
# oop project 3




# class Nigger:
#     Nigger = "Nigga"
#     @staticmethod # revoked the usage of self
#     def getgud():
#         print("You Are A Nigga")      
# aditya = Nigger()
# aditya.getgud()







# class Programmer:
#     Company = "Microsoft"
    
#     def __init__(self, name, language, unit):
#         self.language = language
#         self.name = name
#         self.unit = unit 
        

# # details
#     print("Staff Details")
#     def getInfo(self):
#         print(f'''
      
#   Name = {self.name}
#   Language = {self.language}
#   Unit = {self.unit}     
#           ''')
# edward = Programmer("Edward", "C, C++ and C#", "XBox")
# james = Programmer("James", "Java", "Minecraft Java")
# jack = Programmer("Jack", "C, C++, C#, Go, Java, JavaScript, PHP, Python, Ruby, Scala, and TypeScript", "GitHub")


# edward.getInfo()
# james.getInfo()
# jack.getInfo()




# class calculator:
#     def __init__(self, num):
#         self.number = num
#     def square(self):
#         print(f"the sqaure of {self.number} is {self.number **2}")
    
#     def squareRoot(self):
#         print(f"the sqaure_root of {self.number} is {self.number **0.5}")
    
#     def cube(self):
#         print(f"the cube of {self.number} is {self.number **3}")





# sq = int(input("Enter the number of which you want sqaure of\n"))
# a = calculator(sq)
# a.square()
# a.squareRoot()
# a.cube()









# class Sample():
#     a = "Aero"
    


# obj = Sample()
# obj.a = "Neetu"
# print(Sample.a)
# print(obj.a)

# # end









class Train():
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats 
    
    def getStatus(self):
        print(f'''
        **{self.name}**              
    Engine Name: {self.name}
    Seats Available: {self.seats}          
----------------------------------                
              ''')


    def fareInfo(self):
        print(f'''
        **Fare**      
    Ticket Price: Rs.{self.fare}   
----------------------------------           
              ''')
        
    def bookTicket(self):
        if (self.seats>0):
            self.seats = self.seats - 1
            print(f'''
            **Reservation**      
    Ticket Booked Successfully!
    Seat Number: {self.seats}
----------------------------------    
                  ''')
        else:
            print("Ticket Booked Unsuccessfully [out-of-seats]")
            
            
intercity = Train("Intercity Express: 241122", 90, 2)
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()
# intercity.bookTicket()
# intercity.bookTicket()