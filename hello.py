
import requests 
import math
from math import sqrt, pi
import random
from random import randint, choice



number = random.randint(1, 100)  # Example usage of the random module
choice_list = ['apple', 'banana', 'cherry']
random_choice = random.choice(choice_list)     # Example usage of the random module




math.sqrt(16)  # Example usage of the math module

try:
    response = requests.get("https://api.github.com", timeout=10)
    print("GitHub API Response Status Code:", response.status_code)
except requests.exceptions.RequestException as exc:
    print("Failed to retrieve GitHub data:", exc)

def greet():
    print("Hello, World!")
    pass

greet()

def check_weather():
    teperature = 25  # Placeholder for actual temperature data
    if teperature > 30:
        print("It's hot outside!")  
    else:
        print("The weather is pleasant.")

check_weather()

def greet_user(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")
    pass
greet_user("Alice", "Smith")
greet_user("Bob", "Johnson")

greet_user(first_name="Charlie", last_name="Brown")

def calculate_total(prices, tax_rate,dicount):
    total = sum(prices) * (1 + tax_rate) * (1 - dicount)
    print(f"Total: {total:.2f}")

calculate_total([10.99, 5.49, 3.99], tax_rate=0.07, dicount=0.1)


def create_profile(name, age, city):
    print(f"Profile: {name}, Age: {age}, City: {city}")

create_profile("David", 30, "New York")


def simple_function():
    number = [1, 2, 3, 4, 5]
    first_element = number[0]
    last_element = number[-1]
    return first_element, last_element

first, last = simple_function()
print(f"First Element: {first}, Last Element: {last}")

# return vs print
# The 'return' statement is used to send a value back from a function to the caller.
# The 'print' function is used to display output to the console.

# Extend Python with packages and libraries to enhance functionality. 
# For example, you can use libraries like NumPy for numerical 
# computations, Pandas for data manipulation, Matplotlib for data 
# visualization, and many others.


def get_weather_data(latitude, longitude):
    #
    # url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"

    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m")
    weather_data = response.json()
    return weather_data['hourly']['temperature_2m']  # Initialize weather_data to None
   
get_weather_data(48.85, 2.35)[:10]# Example usage of the get_weather_data function with New York City coordinates, retrieving the first 10 temperature values