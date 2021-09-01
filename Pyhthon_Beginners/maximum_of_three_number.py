''' This is a program to find largest among three the numbers'''

first_num= int(input("Enter the first num"))
second_number= int(input("Enter the second num"))
third_number= int(input("Enter the third number"))
type(third_number)
if first_num>second_number and first_num>third_number:
    print("The greatest number is :" , first_num)
elif second_number>first_num and second_number>third_number:
    print("The greatest number is :" , second_number)
else :
    print("The greatest number is :" , third_number)

