# Program coding:
def count_v2(dna,base):
    i=0 
    for c in dna:
        if c==base:
            i+=1
    return i
dna='ATGCGGCCTAT'
base='C'
n=count_v2(dna,base)
#print-style formatting
print ('%s appears %d times in %s' %(base,n,dna))

# Output:
# C appears 3 times in ATGCGGCCTAT
