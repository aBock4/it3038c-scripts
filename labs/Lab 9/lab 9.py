
#run lab9API.js before running this script
import json

import requests

#url set to local host
r = requests.get('http://localhost:3000/')

data=r.json()
 
 #simple range function to loop through the JSON data and format friendly message
 #instead of writing out 4 seperate print statments
for x in range(4):
    print(data[x]['name'] + " is " + data[x]['color'] + ".")
