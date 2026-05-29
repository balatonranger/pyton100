capitals = {
    "France": "Paris",
    "Spain": "Madrid",
    "Italy": "Rome",
    "Germany": "Berlin",
    "Portugal": "Lisbon"
}
#nested list in dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#print Lille
print(travel_log["France"][1])

nested_list = [ "A", "B", ["C", "D", "E"] ]
print(nested_list[2][1])


travel_log2 = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    } ,
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}

print(travel_log2["Germany"]["cities_visited"][1])