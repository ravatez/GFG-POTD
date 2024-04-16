
from typing import List


class Solution:
    def minimizeDifference(self, n : int, k : int, arr : List[int]) -> int:
        # code here
        post_max = [0] * n
        post_min = [0] * n
        post_max[n-1] = arr[n-1]
        post_min[n-1] = arr[n-1]

        for i in range(n-2, -1, -1):
            post_max[i] = max(arr[i], post_max[i+1])
            post_min[i] = min(arr[i], post_min[i+1])

        ans = post_max[k] - post_min[k]

        maxi = arr[0]
        mini = arr[0]

        for i in range(1, n-k):
            ans = min(ans, max(post_max[i+k], maxi) - min(post_min[i+k], mini))
            maxi = max(arr[i], maxi)
            mini = min(arr[i], mini)

        ans = min(ans, maxi - mini)

        return ans



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
        res = obj.minimizeDifference(n, k, arr)
        
        print(res)
        

# } Driver Code Ends