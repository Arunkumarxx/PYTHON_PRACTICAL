# Program coding:
n=int(input("Enter the upper limit:"))
print("Prime numbers ")
for num in range(0,n+1):
  if num>1:
    for i in range(2,num):
       if(num%i)==0:
        break 
    else: 
       print(num)

#  Output: 

# Enter the upper limit: 5
# Prime numbers:
# 1
# 2
# 3 
