
from typing import List


class Solution:
    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        # code here
        l, h = 0, n-1
        res = -1
        
        while l <= h:
            m = l+(h - l)//2
            if arr[m] == k:
                return k
            if arr[m] <= k:
                if res == -1 or abs(res - k) > abs(arr[m] - k):
                    res = arr[m]
                l = m + 1
            else:
                if res == -1 or abs(res - k) >= abs(arr[m] - k):
                    res = arr[m]
                h = m - 1
        return res
                
                



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        k = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.findClosest(n, k, arr)
        
        print(res)
        

# } Driver Code Ends