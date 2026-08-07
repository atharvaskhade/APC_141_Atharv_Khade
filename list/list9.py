# Create a list of cities

cities = ["Mumbai", "Pune", "Delhi", "Chennai", "Kolkata"]

# Ask the user to enter a city name
city = input("Enter a city name: ")

# Check whether the city exists in the list
if city in cities:
    print(city, "exists in the list.")
else:
    print(city, "does not exist in the list.")