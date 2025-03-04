import bisect
class Solution:
    def lis(self, arr):
        # code here
        sub = []  # This list will store the smallest possible tail for all increasing subsequences of various lengths.
        for x in arr:
            # Use binary search to find the insertion point of x in sub.
            pos = bisect.bisect_left(sub, x)
            if pos == len(sub):
                # x is greater than all elements in sub, extend the list.
                sub.append(x)
            else:
                # Replace the element at the found position with x.
                sub[pos] = x
        # The length of sub is the length of the longest increasing subsequence.
        return len(sub)       



#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    for _ in range(int(input())):
        a = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.lis(a))
        print("~")
# } Driver Code Ends