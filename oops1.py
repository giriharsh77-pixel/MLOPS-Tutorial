#initiate a class
class employee:
    #special method/magic method/dunder method - constructor
    def __init__(self):
        print("started executing attributes/data")
        print(id(self))
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes/data have been initiated")
        
    def travel(self,destination):
        print("This travel method was called Manually")
        print(f"Employee is now travelling to {destination}")

#create an object/instance of class
# all the data and attributes inside the functions is called automatically as soon as class is created.COnstructors are called so that some functions should be connected as soon as the constructor is initiated, user is not expected to do it manually, facebook gets connected to internet as soon as it is opened.
sam = employee()
shaktimaan = employee()
print(id(sam))
print(id(shaktimaan))
# #print(sam.id)
# #print(sam.id) 
print(sam.travel("Kerala"))

# print(type(sam))

# sam.name = "Sam Kumar"

# print(sam.name)