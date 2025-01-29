#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends
#User function Template for python3
class Solution:
    def power(self, b: float, e: int) -> float:
        # Code Here
        def fun(b,e):
            if e==1:
               return b
            if e==0:
                return 1
            prod=1
            if e&1:
                prod*=b
                e-=1
            half=fun(b,e//2)
            return half*half*prod
        if e<0:
            b=1/b
            e=-e
        return fun(b,e)
        

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        b = float(input())
        e = int(input())
        ob = Solution()
        result = ob.power(b, e)
        print(f"{result:.5f}")
        print("~")
# } Driver Code Ends