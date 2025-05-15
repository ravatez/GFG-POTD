from collections import defaultdict
class Solution:
	def countSubstring(self, s):
		# code here
        d = defaultdict(int)
        count = 0
        for i in s:
            d[i] += 1
            count += d[i]
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.countSubstring(s)

        print(answer)
        print("~")

# } Driver Code Ends