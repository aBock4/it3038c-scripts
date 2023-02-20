#This plugin can alter the color of text in the console window

#First PSWriteColor can be used to change one piece of text to one color.
#This will change the text "This is all blue" to the color blue in the console:
Write-Color -Text "This is all blue" -Color Blue

#PSWriteColor can also change multiple pieces of text to multiple colors
#This will change the text "This is red" to red, "This is Green" to green, and "This is magenta" to magenta
#It takes several paramaters as follows:
Write-Color -Text "This is red. ", "This is green. ", "This is magenta." -Color Red,Green,Magenta


#Another example of PSWriteColor is changing the color of the background
#This will change the text "My background color is green!" to have a background of green
Write-Color -Text "My background color is green!" -Background Green

#The last example of PSWriteColor is changing the color of the text and the background
#THis will change the text "I am red with a background color of red." to have red text and a yellow background
Write-Color -Text "I am red with a background color of yellow." -Color Red -Background Yellow