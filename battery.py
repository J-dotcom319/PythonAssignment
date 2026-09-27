class Battery:  
    """A simple attempt to model a battery for an electric car."""  
      
    def __init__(self, battery_size=40):  
        self.battery_size = battery_size  
      
    def describe_battery(self):  
        print(f"This car has a {self.battery_size}-kWh battery.")  
      
    def get_range(self):  
        if self.battery_size == 40:  
            range = 150  
        elif self.battery_size == 65:  
            range = 225  
        print(f"This car can go about {range} miles on a full charge")  
      
    def upgrade_battery(self):  
        """Upgrade the battery to a larger size if possible."""  
        if self.battery_size < 65:  
            print("Upgrading battery to 65-kWh...")  
            self.battery_size = 65  
            print("Battery upgrade complete!")  
        else:  
            print("Battery is already at maximum capacity.")  