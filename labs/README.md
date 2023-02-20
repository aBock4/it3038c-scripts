# Lab 7 Example

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
In this example Write-Color takes in 2 paramaters, Text and Color. The Text is what will be written to the console, and the Color is what color that text will show as.

Now, what if we want to have multiple pieces of text on one line, but each section different colors?
The following Powershell command changes multiple pieces of text to multiple colors in the console.

```powershell
Write-Color -Text "This is red. ", "This is green. ", "This is magenta." -Color Red,Green,Magenta
```
In this example Write-Color still took in 2 paramaters, Text and Color. Howerver, each 'section' of Text is seperated by commas. The Colors are also seperated by commas, in the order that the sections should be colored.

Now, what if we want to change the background of text?
The following Powershell command changes the background color of a piece of text in the console

```powershell
Write-Color -Text "My background color is green!" -Background Green
```
