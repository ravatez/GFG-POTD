#User function Template for python3
class Solution:
	def removeDups(self, str):
		# code here
        lst = [ ]
        for i in s:
            if i in lst:
                continue
            else:
                lst.append(i)
        fstr = "".join(lst)
        return fstr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeDups(s)

        print(answer)

# } Driver Code Ends