#User function Template for python3

class Solution:
    def maxVolume(self, perimeter, area):
        #code here
            # Calculate length l using the formula derived from perimeter and area
        l = (perimeter - math.sqrt(perimeter * perimeter - 24 * area)) / 12
        
        # Calculate height h using the formula for height in terms of l
        h = (perimeter / 4) - (2 * l)
        
        # Calculate volume V using the formulas for length, height, and width (l, l, h)
        V = l * l * h
        
        return V

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        perimeter, area = [int(x) for x in input().split()]

        ob = Solution()
        print('%.2f' % ob.maxVolume(perimeter, area))

# } Driver Code Ends