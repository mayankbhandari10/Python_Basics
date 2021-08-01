#This program creates a stylish font in Python Output
#PyFiglet is helpfull in this

#http://www.figlet.org/fontdb.cgi (Font documentation)


import pyfiglet
name=input("Enter the name")
font=pyfiglet.figlet_format(name,font = "slant")
print(font)