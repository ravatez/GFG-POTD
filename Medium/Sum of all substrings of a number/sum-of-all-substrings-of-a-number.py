#User function Template for python3

class Solution:
    #Function to find sum of all possible substrings of the given string.
    def sumSubstrings(self,s):
        
            # code here
        totalSum = 0
        sumAtIndex = [0] * len(s)
        sumAtIndex[0] = totalSum = ord(s[0]) - ord('0')
    
        for i in range(1, len(s)):
            sumAtIndex[i] = ((i + 1) * (ord(s[i]) - ord('0')) + 10 * sumAtIndex[i - 1]) % (10**9 + 7)
            totalSum = (totalSum + sumAtIndex[i]) % (10**9 + 7)
    
        return totalSum


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s = str(input())
        ob=Solution()
        print(ob.sumSubstrings(s))
# } Driver Code Ends