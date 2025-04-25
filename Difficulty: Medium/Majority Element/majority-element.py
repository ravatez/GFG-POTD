#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        #code here
        cnt, element = 0, -1
        for e in arr:
            if e == element or cnt == 0:
                cnt += 1
                element = e
            else:
                cnt -= 1
        
        return element if arr.count(element) > len(arr)/2 else -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
from sys import stdin


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(arr))
        print("~")
        t -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends