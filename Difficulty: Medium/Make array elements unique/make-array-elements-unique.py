#User function Template for python3

class Solution:
    def minIncrements(self, arr): 
        # Code here
        tmp=[]
        
        arr.sort()
        
        cnt=0
        
        for i in arr:
            if tmp and tmp[-1]>=i:
                c = tmp[-1]-i+1
                cnt+=c
                i+=c
            tmp.append(i)
            
        
        return cnt

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.minIncrements(arr))

        T -= 1

# } Driver Code Ends