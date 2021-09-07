'''Always close the file after ending the program
1) We are opening the file here 'r' means read mode.
deafult mode is read. 'W' is for write
'''

fhand= open('sample.txt','r')
data=fhand.read()
#print(data)
count=0
# To count number of lines in a file.
for line in fhand:
    count=count+1
   # print("Line count",count)


#to split a file content in a list
list_count=[]
lists_cont= data.split('.')
#print(lists_cont)
for list in lists_cont:
    #print(len(list_cont)) # this will give the size of a list
    print(list[1])
