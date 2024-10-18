#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    def getSingle(self,arr):
        # code here
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1
            
        for x in freq:
            if freq[x]==1:
                return x
        for x in freq:
            if freq[x]%2!=0:
                return x
        return 0


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        # k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.getSingle(arr)
        print(res)
        t -= 1


# } Driver Code Ends