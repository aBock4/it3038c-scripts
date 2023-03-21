# Project 2

### What this script does:
This script uses an API and returns data into an organized table.

The API used was provided by: https://www.openbrewerydb.org/

The script gets a list of breweries in a city that the user specifies through user input.

### How to run:
This script will require a Python library download. I will give directions on how to run this script on a Windows machine.

The python library to be downloaded is called "tabulate".  
To download on a windows machine, run the following command in Powershell:

```powershell
pip install tabulate
```
Depending on the permissions, you may need to run as administrator.
If you have another machine, you may follow this link for further documentation: https://pypi.org/project/tabulate/

Run the script using Python (you should already have it installed in your windows Virtual Machine on UC's sandbox):

```python
python project2.py
```
You may have to change the file path!


###  The output:
An example of an output can be as follows (I chose to search "Cincinnati":

![Screenshot 2023-03-20 215005](https://user-images.githubusercontent.com/82166772/226501194-316a1dd3-fb65-47a9-ae53-d043c4367fa7.png)

### References:
https://stackoverflow.com/users/1832058/furas from https://stackoverflow.com/questions/73263371/how-to-add-multiple-values-to-tabulate-array-from-a-range aided in the creation of the table.
