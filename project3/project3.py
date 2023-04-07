from functions import *

#What this script does
print("This script utilizes an API to get a list of breweries by name, state, city, or type.")

choices = ['name','state','city','type']

showChoices()

#boolean to move forward with search
moveOn = False

#if its false keep asking 
while moveOn == False:
    choice = input("What would you like to search by? Your choices are above: ")
    #if the user input is in the array of choices, then set moveOn to true and continue through script
    if choice.lower() in choices:
        moveOn = True
    #else error message and retry
    else:
        print("There was an error in your input. Please only type 1 of these options: 'Name', 'State', 'City', or 'Type'")
        
if choice.lower() == "name":
    name = input ("Please enter a name of a brewery to search for: ") 
    searchByName(name)
elif choice.lower() == "state":
    state = input ("Please enter a FULL STATE name to search for breweries in: ") 
    searchByState(state)
elif choice.lower() == "city":
    city = input ("Please enter a city to search for breweries in: ") 
    searchByCity(city)
else:
    showTypes() 
    
    choices = ['micro','nano','regional','brewpub','large','planning','bar','contract','propietor','closed']
    
    #boolean to move forward with search
    moveOn = False

    #if its false keep asking 
    while moveOn == False:
        bType = input("Please enter a type of a brewery to search for. Your choices are above: ")
        #if the user input is in the array of choices, then set moveOn to true and continue through script
        if bType.lower() in choices:
            moveOn = True
        #else error message and retry
        else:
            showTypes()
            print("There was an error in your input. Please only type 1 of the choices above: ")
    searchByType(bType)
