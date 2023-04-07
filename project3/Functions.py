def responseStatus(response):
    #some error handling
    if response.status_code > 300:
        print("There was an error in the request. Please try again.")
    else: 
        json = response.json()
        return json
