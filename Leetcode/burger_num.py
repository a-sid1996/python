# Number of Burgers with No Waste of Ingredients (LC 1276)

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # 4x + 2y = tomatoSlices
        # x + y = cheeseSlices
        x = ( tomatoSlices - 2 * cheeseSlices ) / 2
        y = cheeseSlices -  x
                
        if ( x.is_integer() and y.is_integer() and x >= 0 and y >= 0 ):
            return [int(x), int(y)]
        return []
