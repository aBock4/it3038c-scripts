import requests
from tabulate import tabulate
from Functions import *

#Documentation for API found at: https://www.openbrewerydb.org/documentation

#What this script does
print("This script utilizes an API to get a list of breweries by name, state, city, or type.")

#array of search choices
choices = ["name", "state", "city", "type"]

#boolean to move forward with search
moveOn = False

#if its false keep asking 
while moveOn == False:
    choice = input("Would you like to search by Name, State, City, or Type? ")
    #if the user input is in the array of choices, then set moveOn to true and continue through script
    if choice.lower() in choices:
        moveOn = True
    #else error message and retry
    else:
        print("There was an error in your input. Please only type 1 of these options: 'Name', 'State', 'City', or 'Type'")
        
if choice.lower() == "name":
    name = input ("Please enter a name of a brewery to search for: ") 
elif choice.lower() == "state":
    state = input ("Please enter a FULL STATE name to search for breweries in: ") 
    
    #cap this at 100 because it can be lengthy
    response = requests.get('https://api.openbrewerydb.org/breweries?by_state=' + state.lower() + '&per_page=100')
    
    json = responseStatus(response)
    
    #create a table with 3 headers
    table = [
        ['Brewery:', 'Street:', 'City:', 'State:', 'Zip Code:']
    ]

    #add brewery, street, and zip code to each row
    for model in json:
        row = [
            model['name'],
            model['street'],
            model['city'],
            model['state'],
            model['postal_code']
        ]
        table.append(row)

    #Print the table to the console
    print(tabulate(table, tablefmt='fancy_grid'))
    
elif choice.lower() == "city":
    city = input ("Please enter a city to search for breweries in: ") 
    
    response = requests.get('https://api.openbrewerydb.org/breweries?by_city=' + city.lower())
    print(city)
    
    json = responseStatus(response)
    

    #create a table with 3 headers
    table = [
        ['Brewery:', 'Street:', 'City:', 'State:', 'Zip Code:']
    ]

    #add brewery, street, and zip code to each row
    for model in json:
        row = [
            model['name'],
            model['street'],
            model['city'],
            model['state'],
            model['postal_code']
        ]
        table.append(row)

    #Print the table to the console
    print(tabulate(table, tablefmt='fancy_grid'))
else:
    type = input ("Please enter a type of a brewery to search for: ") 
