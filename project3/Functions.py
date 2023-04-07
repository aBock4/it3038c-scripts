import requests
from tabulate import tabulate


def showChoices():
    #array of search choices
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

def responseStatus(response):
    #some error handling
    if response.status_code > 300:
        print("There was an error in the request. Please try again.")
    else: 
        json = response.json()
        return json

def printTable(json):
    #create a table with 3 headers
    table = [
        ['Brewery:', 'Street:', 'City:', 'State:', 'Zip Code:', 'Website URL:']
    ]

    #add brewery, street, and zip code to each row
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
def searchByName(name):
    response = requests.get('https://api.openbrewerydb.org/breweries?by_name=' + name.lower() + '&per_page=100')
    
    json = responseStatus(response)
    
    printTable(json)
    
def searchByCity(city):
    response = requests.get('https://api.openbrewerydb.org/breweries?by_city=' + city.lower())
    
    json = responseStatus(response)
    
    printTable(json)

def searchByState(state):
    #cap this at 100 because it can be lengthy
    response = requests.get('https://api.openbrewerydb.org/breweries?by_state=' + state.lower() + '&per_page=100')
    
    json = responseStatus(response)
    
    printTable(json)

def searchByType(bType):
    #cap this at 100 because it can be lengthy
    response = requests.get('https://api.openbrewerydb.org/breweries?by_type=' + bType.lower() + '&per_page=100')
    
    json = responseStatus(response)
    
    printTable(json)

def showTypes():
    #create a table with 3 headers
    table = [
        ['Choice:', 'What it means:']
    ]

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
