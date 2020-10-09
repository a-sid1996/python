# find missing numbers in array (LC 448)

def findDisappearedNumbers(nums):
    l = [i+1 for i in range(len(nums))]
    for i in nums:
        l[i-1] = None
    return [i for i in l if i is not None]
    
a = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(a))
