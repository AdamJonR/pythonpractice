# Simple car class that includes accelerating and braking capabilities
class Car:
    def __init__(self, year_model, make):
        # Initialize the Car object with the given year_model and make
        self.__year_model = year_model
        self.__make = make
        # Initialize the current speed to 0
        self.__speed = 0   
        # Define the speed increment/decrement value
        self.__jump = 5     

    #
    def accelerate(self):
        # Increase the car's speed by the value of __jump
        self.__speed += self.__jump
    
    #
    def brake(self):
        # Decrease the car's speed by the value of __jump
        self.__speed -= self.__jump
    
    #
    def get_speed(self):
        # Return the current speed of the car
        return self.__speed
