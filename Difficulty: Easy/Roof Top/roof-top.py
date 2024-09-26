#User function Template for python3

class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self, arr):
        #Your code here
        n = len(arr)
        cnt = 0
        maxi = 0
        for i in range(n-1):
            if arr[i] < arr[i+1]:
                cnt += 1
            else:
                maxi = max(maxi,cnt)
                cnt = 0
        maxi = max(maxi,cnt)
        return maxi

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maxStep(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends