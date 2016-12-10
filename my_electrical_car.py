from electrical_car import ElectricalCar

my_tesla = ElectricalCar('tesla', ' model s', 2016)
my_tesla.battery.update_battery()
my_tesla.battery.get_range()
print my_tesla.get_descriptive_name()
