import requests
from tabulate import tabulate

#What this script does
print("This script utilizes an API to get a list of breweries in a city of your choice.")

#Get user input for city to search
city = input("Please enter a city to search for breweries in: ")

response = requests.get('https://api.openbrewerydb.org/breweries?by_city=' + city)

#some error handling
if response.status_code > 300:
    print("There was an error in the request. Please try again.")
else: json = response.json()

#Function to get json data and store in arrays
#This fuction is not used
#I plan on using it to expand on this in project 3!
def getJSONData(response):
    #Put all the names in an array
    breweries = []
    for b in json:
        brewery = b['name']
        breweries.append(brewery)

    #Put all streets in an array
    streets = []
    for s in json:
        street = s['street']
        streets.append(street)

    #put the postal codes in an array
    postals = []
    for p in json:
        postal = p['postal_code']
        postals.append(postal)
    
#create a table with 3 headers
table = [
    ['Brewery:', 'Street:', 'Zip Code:']
]

#add brewery, street, and zip code to each row
for model in json:
    row = [
        model['name'],
        model['street'],
        model['postal_code']
    ]
    table.append(row)

#Print the table to the console
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
    
