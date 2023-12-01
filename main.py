travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hambrug", "Stuttgart"]
    }
]

country = str(input(">>country : "))
visits = int(input(">>visits : "))
cities = input(">>cities city1,city2: ").split(",")
trimmed_cities = [city.strip() for city in cities]

def merge_array(array1, array2):
    merged_array = array1.copy()
    for element in array2:
        if element not in merged_array:
            merged_array.append(element)
    
    return merged_array

def addTravel(country, visits, trimmed_cities):
    check_data = False
    for data in travel_log:
        if country in data["country"]:
            newCity = merge_array(data["cities"], trimmed_cities)
            print(newCity)
            data["cities"] = newCity   
            data["visits"] += visits
            check_data = True
            break
    
    if check_data == False:
        newData = {
            "country": country,
            "visits": visits,
            "cities": trimmed_cities
        }
        travel_log.append(newData)
    print(travel_log)


addTravel(country, visits, trimmed_cities)