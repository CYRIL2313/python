#Author:cyril
#Date:19-10-2024
#Description:Create, concatenate, and print a string and access a sub-string from a given string.


first_name=input("Enter your first name:")
last_name=input("Enter your last name:")
name=first_name+" "+last_name
print(name)
last_name_length=len(last_name)
print(last_name_length)
extracted_first_name=name[:last_name_length]
print(extracted_first_name)
first_name_length=len(first_name)
print(first_name_length)
extracted_last_name=name[first_name_length+1:]
print(extracted_last_name)
