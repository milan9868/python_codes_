class Employee:
    company = "Google"
    user = "Swasti"
    
    def showDetails(self):
        print(f"{self.user} Joined {self.company}, lol")
        
class Programmer(Employee):
    language = "Java"
    
    def getLanguage(self):
        print(f"The Language used by the employee {self.user} is {self.language}")
        
class Freelancer(Programmer, Employee):
    platform = "Fiverr"
    platform2 = "Discord"
    level = 0
    
    def addLvl(self):
        while (self.level<3):
            self.level = self.level + 1
    
    def getPlatform(self):
        print(f"\n {self.user} is also a freelancer\n Platform = {self.platform}, {self.platform2}\n Seller level on {self.platform} is {self.level} ")       
   
    
swasti = Employee()
swasti = Programmer()
swasti.showDetails()
swasti.getLanguage()
swasti = Freelancer()
swasti.addLvl() 
swasti.getPlatform()

# class using inheritance method




# class C2dVec:
#     def __init__(self, i, j):
#         self.icap = i
#         self.jcap = j

#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j"

# class C3dVec(C2dVec):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.kcap = k
    
#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
    
    
# v2d = C2dVec(1, 3)
# v3d = C3dVec(1, 9, 7)
# print(v2d)
# print(v3d)



from playsound import playsound
class Animal:
    AnimalType = "Mamal"
    
class Pets(Animal):
    PetType = "Vegeterian"
    
class Dog(Pets):
    @staticmethod
    def bark():
        # playsound("F:/Coding/bark.mp3")
        print("Bow Bow!")
        
    
d = Dog()
d.bark()
# Ends Here, Multilevel Inheritance
    




































