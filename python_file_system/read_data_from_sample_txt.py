'''Always close the file after ending the program
1) We are opening the file here 'r' means read mode.
'''

f= open('sample.txt','r')
data=f.read()
print(data)
f.close()