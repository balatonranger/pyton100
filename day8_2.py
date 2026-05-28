def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"How are you {name}? ")
    print(f"Isn't the weather nice in {location} today?")

# greet_with_name("Alice", "New York")  # This will raise an error because the function expects two arguments but only one is provided.
greet_with_name("Alice", "New York")  # This will work correctly because both required arguments are provided.
