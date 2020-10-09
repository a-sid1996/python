# Simplified Fractions (LC 1447)

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
    
########## simplified ###############

        l = []
        for i in range(2, n+1):
            for j in range(1, i):
                if math.gcd(i, j) < 2:
                    l += [f'{j}/{i}']
        return l

########## Dynamic programming solution ##########

#         def memoize(f):
#             memo = {}
#             def helper(x):
#                 if x not in memo:            
#                     memo[x] = f(x)
#                 return memo[x]
#             return helper
        
#         def hcf(a, b):
#             for i in range(2, a+1):
#                 if a % i == 0 and b % i == 0:
#                     return False
#             return True

#         def cal(x):
#             l = []
#             for i in range(1, x):
#                 if hcf(i, x):
#                     l += ["{}/{}".format(i, x)]
#             return l

#         def foo(n):
#             if n == 1:
#                 return []
#             elif n == 2:
#                 return ["1/2"]
#             else:
#                 return foo(n-1) + cal(n)

        
#         foo = memoize(foo)
        
#         return foo(n)
