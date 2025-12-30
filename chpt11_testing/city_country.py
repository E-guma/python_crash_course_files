"""This Module contains "city_country()" to return "City, Country" """

def city_country(city, country, population = None):
    """Returns City, Country, and population in passed"""
    if population:
        location = f"{city}, {country} - population {population}"
    else:
        location = city + ", " + country
    return location.title()
    
if __name__ == '__main__':
    print(city_country('lagos', 'nigeria', 50000))
    