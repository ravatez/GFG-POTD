#User function Template for python3


class Solution:
    
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        #defining a function instead of using sort() because of expected time complexity
        def order(x,y):
            if x > y :
                t = y
                y = x
                x = t
            return (x,y)

        (x,y)=order(x,y)
        (y,z)=order(y,z)
        (x,y)=order(x,y)
        
        r = n%x
        q = int(n/x)
        
        #if n is divible by smallest number in the given set of three number then it is best case
        if r == 0:
            return q
        
        val =0
        for i in range(q+1):
            if (r+(i*x))%y == 0:
                val = q-i + int((r+i*x)/y)
                break
        i = 0
        for i in range(q+1):
            if (r+(i*x))%z == 0:
                val = max(val,q-i + int((r+i*x)/z))
                break
        i = 0
        for i in range(q+1):
            if (r+(i*x))%(y+z) == 0:
                val =max(val, q-i+1 + int((r+i*x)/(y+z)))
                break
        return val

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        x,y,z=[int(x) for x in input().split()]
        
        print(Solution().maximizeTheCuts(n,x,y,z))
# } Driver Code Ends