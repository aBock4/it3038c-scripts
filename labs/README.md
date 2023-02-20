# Lab 7 

Here is how you can run a Powershell script that I created, which uses a plugin called PSWriteColor. This plugin can alter the color of text in the console window

First, let's download the plugin. Open up Powershell and run the following command: 

```powershell
Install-Module -Name PSWriteColor
```
Depending on the permissions, you may need to run as administrator

The following Powershell command changes one piece of text to one specific color in the console.

In powershell, run the following code:

```powershell
Write-Color -Text "This is all blue" -Color Blue
```
In the above example Write-Color takes in 2 paramaters, Text and Color. The Text is what will be written to the console, and the Color is what color that text will show as.

Now, what if we want to have multiple pieces of text on one line, but each section different colors?
The following Powershell command changes multiple pieces of text to multiple colors in the console.

```powershell
Write-Color -Text "This is red. ", "This is green. ", "This is magenta." -Color Red,Green,Magenta
```
In the above example Write-Color still took in 2 paramaters, Text and Color. Howerver, each 'section' of Text is seperated by commas. The Colors are also seperated by commas, in the order that the sections should be colored.

Now, what if we want to change the background of text?
The following Powershell command changes the background color of a piece of text in the console

```powershell
Write-Color -Text "My background color is green!" -Background Green
```
In the above example Write-Color took in 2 paramaters, Text and Background. The Text is what will be written to the console, and the Background is what color that the background of the text will be.

Now what if we wanted to have both a backgorund color and a different colored text?
The followoing powershell command does just that.

```powershell
Write-Color -Text "I am red with a background color of yellow." -Color Red -Background Yellow
```
In the above example Write-Color took in 3 paramaters, Text, Color and Background. The Text is what will be written to the console, the Color is what color the text will show as, and the Background is what color that the background of the text will be.
