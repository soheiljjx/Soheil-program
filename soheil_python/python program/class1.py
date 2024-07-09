class Car:
    def __init__(self,model,brand,years):
        self.model=model
        self.brand=brand
        self.years=years
    def print_car(self):
        print(f"the car is {self.model}and the{self.brand} and the{self.years}")
    def year(self):
        print(self.years*10)
car1=Car("x3","BMW",2022)
car1.print_car()
car1.year()
    
