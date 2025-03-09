#User function Template for python3

class Solution:

    def countPS(self, s):
        # code here
        res, n = 0, len(s)
        def pal(i, j):
            count = 0
            while i >= 0 and j < n and s[i] == s[j]: 
                count,i,j = count + 1,i - 1,j + 1
            return count
        for i in range(n):
            res += pal(i, i)      
            res += pal(i, i + 1)  
        return res - n  # Exclude single character palindromes

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.countPS(s))

        print("~")
# } Driver Code Ends