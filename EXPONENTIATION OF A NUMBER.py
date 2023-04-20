# Program coding:
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):	
        return(base*power(base,exp-1))
base=int(input("Enter base:"))
exp=int(input("Enter exponential value:"))
print("result:",power(base,exp))

# Output:

# Enter base: 7
# Enter exponential value: 2
# Result:49
