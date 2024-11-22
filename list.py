from PIL.ImImagePlugin import number
from babel.numbers import format_number
from uaclient.system import should_reboot

# AUTHER:CYRIL
# DATE:22/11/2024
# DESCRIPTION:Input two list from the user.Merge these list into a third list such that
# in the merged list,all even numbers occure first followed by odd number.both the even numbers
# and odd number should be in sorted format.
list1=[1,2,2,5,3,7,4,3,5,32,45]
list2=[24,76,3,1,2,3,4,44,56]
original_list=list1+list2
even=[]
odd=[]
for number in original_list:
    if number%2==0:
        even.append(number)
    else:
        odd.append(number)
even.sort()
odd.sort()
oddeven=even+odd
print("first list")
print(list1)
print("second list")
print(list2)
print("final list")
print(oddeven)