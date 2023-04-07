import requests
from tabulate import tabulate

#Documentation for API found at: https://www.openbrewerydb.org/documentation

#function to show choices in a table for user
def showChoices():
    #json with search choices
    choices = [{'choice': "name", 'meaning': 'Search by name of brewery'},{'choice': "city", 'meaning': 'Search by city of brewery'},{'choice': "state", 'meaning': 'Search by state of brewery'},{'choice': "type", 'meaning': 'Search by type of brewery'}]
    
    #create a table with 3 headers
    table = [
        ['Choice:', 'What it means:']
    ]
    
    #add data in
    for model in choices:
        row = [
            model['choice'],
            model['meaning']
        ]
        table.append(row)

    #Print the table to the console
    print(tabulate(table, tablefmt='fancy_grid'))

#function to handle bad responses
def responseStatus(response):
    #some error handling
    if response.status_code > 300:
        print("There was an error in the request. Please try again.")
    else: 
        json = response.json()
        return json

#function to print the tables
def printTable(json):
    #create a table with 6 headers
    table = [
        ['Brewery:', 'Street:', 'City:', 'State:', 'Zip Code:', 'Website URL:']
    ]

    #add brewery, street, city, state, zip code, and website url to each row
    for model in json:
        row = [
            model['name'],
            model['street'],
            model['city'],
            model['state'],
            model['postal_code'],
            model['website_url']
        ]
        table.append(row)

    #Print the table to the console
    print(tabulate(table, tablefmt='fancy_grid'))

#function to search the api by names
def searchByName(name):
    #set up url and get json response
    #limit the results to 200
    response = requests.get('https://api.openbrewerydb.org/breweries?by_name=' + name.lower() + '&per_page=200')
    
    #see if the response is good
    json = responseStatus(response)
    
    #call the print table function 
    printTable(json)
    
#function to search the api by city
def searchByCity(city):
    #set up url and get json response
    response = requests.get('https://api.openbrewerydb.org/breweries?by_city=' + city.lower())
    
    #see if the response is good
    json = responseStatus(response)
    
    #call the print table function 
    printTable(json)

#funcion to search the api by state
def searchByState(state):
    #set up url and get json response
    #cap this at 200 because it can be lengthy
    response = requests.get('https://api.openbrewerydb.org/breweries?by_state=' + state.lower() + '&per_page=200')
    
    #see if the response is good
    json = responseStatus(response)
    
    #call the print table function 
    printTable(json)

#function to search the api by type
def searchByType(bType):
#set up url and get json response
    #cap this at 200 because it can be lengthy
    response = requests.get('https://api.openbrewerydb.org/breweries?by_type=' + bType.lower() + '&per_page=200')
    
    #see if the response is good
    json = responseStatus(response)
    
    #call the print table function 
    printTable(json)

#function to show the choices for the types of breweries
def showTypes():
    #create a table with 3 headers
    table = [
        ['Choice:', 'What it means:']
    ]

    #json with choices and meanings of types/options
    types = [{'choice': 'micro', 'meaning': 'Most craft breweries. For example, Samual Adams is still considered a mircro brewery.'},{'choice': 'nano', 'meaning': 'An extremely small brewery which typically only distributes locally.'},{'choice': 'regional', 'meaning': 'A regional location of an expanded brewery. Ex. Sierra Nevada’s Asheville, NC location.'},{'choice': 'brewpub', 'meaning': 'A beer-focused restaurant or restaurant/bar with a brewery on-premise.'},{'choice': 'large', 'meaning': 'A very large brewery. Likely not for visitors. Ex. Miller-Coors'},{'choice': 'planning', 'meaning': 'A brewery in planning or not yet opened to the public.'},{'choice': 'bar', 'meaning': 'A bar. No brewery equipment on premise.'},{'choice': 'contract', 'meaning': 'A brewery that uses another brewery’s equipment.'},{'choice': 'propietor', 'meaning': 'Similar to contract brewing but refers more to a brewery incubator'},{'choice': 'closed', 'meaning': 'A location which has been closed.'}]
    
    #add data in
    for model in types:
        row = [
            model['choice'],
            model['meaning']
        ]
        table.append(row)

    #Print the table to the console
    print(tabulate(table, tablefmt='fancy_grid'))
