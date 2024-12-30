# Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

# 2. Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).

# 3. Inheritance
#  Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

# 4. Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

# 5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

# 6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.

# 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.

# 8. Property Decorators
#  Problem: Use a property decorator in the Car class to make the model attribute read-only.

# 9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Car:
    total_car = 0

    def __init__(self, brand, model): # init ta k akhane "constructor" name porichito
        self.brand = brand
        # nicher brand ta object hisebe access kra jay na... shodhu matro method baniye eti access kra jabe.. an example of encapsulation
        # self.__brand = brand
        # self.model = model
        self.__model = model
        Car.total_car+=1

    # ekta method
    def hello():
        print("hello")

    # getter method starts with get.. similarly setter method starts with set..
    def get_brand(self):
        return self.__brand+" !"

    def fullName(self): # "self" ekta internet line jetar maddhome connection deya hoy
        return f"{self.model} {self.brand}"
    
    def fuel_type(self):
        return "Petrol or diesel"
    
    @staticmethod #decorators
    def general_description():
        return "car are means a lot"
    
    @property
    def model(self):
        return self.__model

# inheritence example
class ElectricCar(Car): 
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "e charge"
    
class Battery:
    def battery_info(self):
        return "der bin battery"

class Engine:
    def engine_info(self):
        return "der bin engine"

class ElectricTwo(Battery, Engine, Car):
    pass

myNewTesla= ElectricTwo("tes", 'model s')
print(myNewTesla.brand)
print(myNewTesla.battery_info())

myTesla = ElectricCar("teshla", "model 5", "85 kWh")
# print(myTesla.model)
# print(myTesla.brand)
# print(myTesla.battery_size)
# print(myTesla.fullName())
# print(myTesla.fuel_type())
print(isinstance(myTesla,ElectricCar))

safari = Car("tata", "safari")
# print(safari.fuel_type())
# print(safari.general_description())

        
# creating instance
my_car = Car("toyota","corolla") # function er vitorer value gulo k variable or attributes name porichito
# my_car.model = "xity"
# print(my_car.model)
# print(my_car.model())
# print(my_car.fullName())
# print(my_car.fuel_type())
# print(my_car.total_car) not a good way to access total car
# print(Car.total_car)

# techSkills = Car("language", "C++")
# print(techSkills.model)
