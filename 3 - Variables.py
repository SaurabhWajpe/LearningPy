no_of_cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90

name, age = 'Saurabh', 33

print "I'm %s and I'm %d years old"%(name, age)  

cars_not_driven = no_of_cars - drivers
car_driven = drivers
carpool_Capacity = car_driven * space_in_car
average_passengers_per_car = passengers / car_driven

print "There are", no_of_cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_Capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Below, "Spaces" will be placed between Test and without and will replace %s
print "Test %s Without" % "Spaces"
