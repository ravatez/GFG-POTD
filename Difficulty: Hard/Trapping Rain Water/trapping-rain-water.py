
class Solution:
    def maxWater(self, arr):
        # code here
        n=len(arr)
        waterFill=0
        lmax,rmax=0,0
        st,end=0,n-1
        while st<end:
            if arr[st]<arr[end]:
                if arr[st]<lmax:
                    waterFill+=lmax-arr[st]
                else:
                    lmax=arr[st]
                st+=1
            else:
                if arr[end]<rmax:
                    waterFill+=rmax-arr[end]
                else:
                    rmax=arr[end]
                end-=1
        return waterFill

#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends