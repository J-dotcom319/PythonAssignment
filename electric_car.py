from car_module import Car  
from battery_module import Battery  
  
class ElectricCar(Car):  
    """Represent aspects of a car, specific to electric vehicles."""  
      
    def __init__(self, make, model, year):  
        super().__init__(make, model, year)  
        self.battery = Battery()  