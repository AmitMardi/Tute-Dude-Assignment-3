# Task 2: Using the Math Module for Calculations
from math import *

def calculate_square_root(num):
    return sqrt(num)

def natural_logarithm(num):
    return log(num)

def sine_in_radians(num):
    return sin(num)

num = int(input("Enter a number: "))
sqrt_result = calculate_square_root(num)
log_result = natural_logarithm(num)
sine_result = sine_in_radians(num)

print("Square root: ", sqrt_result)
print("Natural logarithm: ", log_result)
print("Sine (in radians): ", sine_result)