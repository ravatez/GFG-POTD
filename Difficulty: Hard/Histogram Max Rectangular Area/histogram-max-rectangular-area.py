#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends


class Solution:
    def getMaxArea(self,arr):
        #code here
        mx=0
        stk=[]
        for ix,ve in enumerate(arr):
            while stk and arr[stk[-1]]>=ve:
                stk.pop()
            stk.append(ix)
            for j,ve in enumerate(stk):
                if j==0:
                    mx=max(mx,arr[stk[j]]*(ix+1))
                    continue
                mx=max(mx,(arr[stk[j]])*(ix-stk[j-1]))
        return mx

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.getMaxArea(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends