__author__ = 'Szabo Mate'

cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
car_pool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", car_pool_capacity, "passengers today")
print("We have", passengers, "passengers today")
print("We need to put about", average_passengers_per_car, "passengers in each car")