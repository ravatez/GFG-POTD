
from typing import List


class Solution:
    def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
        # code here
        temp = [[abs(a - b), i] for i, (a, b) in enumerate(zip(arr, brr))]
        temp.sort(reverse=True)
        
        ans = 0
        for _, i in temp:
            if arr[i] > brr[i]:
                if x!= 0:
                    ans += arr[i]
                    x -= 1
                else:
                    ans += brr[i]
                    y -= 1
            else:
                if y!= 0:
                    ans += brr[i]
                    y -= 1
                else:
                    ans += arr[i]
                    x -= 1
        
        return ans



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        x = int(input())

        y = int(input())

        arr = IntArray().Input(n)

        brr = IntArray().Input(n)

        obj = Solution()
        res = obj.maxTip(n, x, y, arr, brr)

        print(res)

# } Driver Code Ends