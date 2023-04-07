# Project 3

### What this script does:
This script uses an API and returns data into an organized table.

The API used was provided by: https://www.openbrewerydb.org/    

This script gets a list of breweries that the user searched for by name, state, city, or type.

### Prerequisites:
This script will require two Python library downloads. I will give directions on how to run this script on a Windows machine.

The first python library to be downloaded is called "tabulate".    
To download on a windows machine, run the following command in Powershell:

```powershell
pip install tabulate
```
Depending on the permissions, you may need to run as administrator. If you have another machine, you may follow this link for further documentation: https://pypi.org/project/tabulate/

You will also need to download the module 'requests'. It can be downloaded with the following command on a windows machine:
```powershell
pip install requests
```
Depending on the permissions, you may need to run as administrator.

### Run the script:
Download both 'project3.py' and 'functions.py' from the repo  

Make sure they are in the same directory, otherwise python will not be able to find the 'functions.py' file!  

Open a powershell window and maximize the window (for the best possible experience :) )  

Run the script using Python (you should already have it installed in your windows Virtual Machine on UC's sandbox):

```python
python project3.py
```
You will most likely have to change the file path, based on where the python file is located on your machine.  
  
Keep in mind that due to the design of the api, the highest number of results that can be returned is 200


###  Examples:
An example of an output can be as follows (I chose to search "Cincinnati":

![Screenshot 2023-03-20 215005](https://user-images.githubusercontent.com/82166772/226501194-316a1dd3-fb65-47a9-ae53-d043c4367fa7.png)

### References:
The documentation that I used for the API: https://www.openbrewerydb.org/documentation   

https://stackoverflow.com/users/1832058/furas from https://stackoverflow.com/questions/73263371/how-to-add-multiple-values-to-tabulate-array-from-a-range aided in the creation of the table.
