# check if array is strictly increasing or decreasing (LC 941)

def checkIncr(A):
    for ind in range(len(A)-1):
        if A[ind] > A[ind+1]:
            return ind
        elif A[ind] == A[ind+1]:
            return -1
    return -1

def checkDecr(A):
    for ind in range(len(A)-1):
        if A[ind] < A[ind+1]:
            return False
        elif A[ind] == A[ind+1]:
            return False
    return True

def validMountainArray(A):
    res = checkIncr(A)
    if res == -1 or res == 0:
        return False
    return checkDecr(A[res:])
    
a = [2,1]
b = [3,5,5]
c = [0,3,2,1]

print(validMountainArray(a)) #false
print(validMountainArray(b)) #false
print(validMountainArray(c)) #true
