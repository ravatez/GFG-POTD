class Solution:
    def wordBreak(self, s, dictionary):
        # code here
        # code here
        st = set(dictionary)
        l, n = len(max(dictionary, key=len)), len(s)

        dp = [False]*(n+1)
        dp[0] = True
        
        for j in range(n):
            for i in range(j, max(-1, j-l), -1):
                dp[j+1] = dp[j+1] or dp[i] and (s[i:j+1] in st)

        return dp[-1]

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_case = int(input())

    for _ in range(test_case):
        s = input().strip()
        dictionary = input().strip().split()
        ob = Solution()
        res = ob.wordBreak(s, dictionary)
        if res:
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends