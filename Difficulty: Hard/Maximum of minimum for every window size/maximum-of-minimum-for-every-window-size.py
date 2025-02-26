
class Solution:
    def maxOfMins(self, arr):
        # code here
        # find the next/pre smaller elements
        # if the length = n window has min value x, 
        # then the length = n-1 window has min value >= x (at least x)
        n = len(arr)
        right = [n]*n
        stack = []
        for i, e in enumerate(arr):
            # don't use arr[stack[-1]] >= e since we are 
            # trying to find the longest window, the shorter 
            # window will automatically work and in the last 
            # step, we can use longest window min value for 
            # shorter window
            while stack and arr[stack[-1]] > e:
                right[stack.pop()] = i 
            stack.append(i)

        left = [-1]*n
        stack = []
        for i in range(n-1, -1, -1):
            e = arr[i]
            while stack and arr[stack[-1]] > e:
                left[stack.pop()] = i
            stack.append(i)

        ans = [0]*n
        for i in range(n-1, -1, -1):
            r = right[i]-left[i]-1
            ans[r-1] = max(ans[r-1], arr[i])

        #this line is not necessary since the minimum value
        #will always have length n
        #ans[-1] = min(arr)
        #print(ans)
        for i in range(n-2, -1, -1):
            ans[i] = max(ans[i], ans[i+1])
   
        return ans

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        solution = Solution()
        result = solution.maxOfMins(arr)
        print(" ".join(map(str, result)))
        print("~")
# } Driver Code Ends