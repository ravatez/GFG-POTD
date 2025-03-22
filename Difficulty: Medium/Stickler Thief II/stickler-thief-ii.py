class Solution:
    def maxValue(self, arr):
        # code here
        def f(ind, dp, arr):
            if ind >= len(arr):
                return 0
            if ind in dp:
                return dp[ind]
            p1 = arr[ind] + f(ind + 2, dp, arr)
            p2 = f(ind + 1, dp, arr)
            dp[ind] = max(p1, p2)
            return dp[ind]

        if not arr:
            return 0

        n = len(arr)
        dp1, dp2 = {}, {}
        v1, v2 = arr[:-1], arr[1:]

        f1 = f(0, dp1, v1)
        f2 = f(0, dp2, v2)

        return max(f1, f2)        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self):
        arr = [int(i) for i in input().strip().split()]
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = IntArray().Input()

        obj = Solution()
        res = obj.maxValue(arr)

        print(res)
        print("~")

# } Driver Code Ends