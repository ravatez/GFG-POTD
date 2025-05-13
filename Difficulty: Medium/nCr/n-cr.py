class Solution:
    def nCr(self, n, r):
        # code here
        if n<r:

            return 0

        elif n==r or r==0:

            return 1

        else:

            numerator=n

            denominator=r

            while(r>1):

                numerator*= (n-1)

                denominator*=(r-1)

                n-=1

                r-=1

            return numerator//denominator 

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        r = int(input())
        ob = Solution()
        print(ob.nCr(n, r))
        print("~")
# } Driver Code Ends