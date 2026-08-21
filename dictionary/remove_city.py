# Create a dictionary of cities and their populations
cities_population = {
    "Tokyo": 37400000,
    "Delhi": 29300000,
    "Shanghai": 26300000,
    "Sao Paulo": 21800000,
    "Mexico City": 21600000
}
print("Original city population:", cities_population)

# Remove a specified city (e.g., "Shanghai")
cities_population.pop("Shanghai")

# Display the updated dictionary
print("Updated city population:", cities_population)
