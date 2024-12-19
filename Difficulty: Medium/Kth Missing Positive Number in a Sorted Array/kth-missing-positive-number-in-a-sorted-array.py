#User function Template for python3
class Solution:
    def kthMissing(self, arr, k):
        # code here
        # code here
        n=len(arr)
        p=arr[-1]-n
        if p<k:
            return arr[-1]+(k-p)
        i=0
        j=1
        while k>0:
            if arr[i]!=j:
                j+=1
                k-=1
            else:
                i+=1
                j+=1
        return j-1 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.kthMissing(A, D)
        print(ans)
        print("~")

# } Driver Code Ends