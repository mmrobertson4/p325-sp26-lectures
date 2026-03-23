class Battery:
        """A simple attempt to model a battery for an electric car"""

        def __init__(self, battery_size=123):
            """Initialize the battery's attributes"""
            self.battery_size = battery_size

        def describe_battery(self):
            """Print a statement describing the battery size"""
            print(f'This car has a {self.battery_size}-kWh battery.')

        def get_range(self):
            if self.battery_size == 123:
                print("Range is 350 miles")
            elif self.battery_size == 170:
                print("Range is 470 miles")
    
        def update_battery(self):
            self.battery_size = 170