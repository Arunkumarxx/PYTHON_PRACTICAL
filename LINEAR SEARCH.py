# Program coding:
items=[5,7,10,12,15]
print("List of items is",items)
x=int(input("Enter item to search:"))
i=flag=0
while i<len(items):
    if items[i]==x:
        flag=1
        break
    i=i+1
if flag==1:
  print("Items found at position:",i+1)
else:
  print("Items not found")
# Output:

#  (List of items is: [5, 7, 10, 12, 15] )
#             Enter item to search: 7
#      (Item found at position: 2)
