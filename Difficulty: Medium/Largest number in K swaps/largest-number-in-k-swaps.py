#User function Template for python3

class Solution:
    
    #Function to find the largest number after k swaps.
    def findMaximumNum(self, s, k):
        #code here
        self.max_num = s

        def helper(s_list, k, index):
            if k == 0 or index == len(s_list):
                return

            max_char = max(s_list[index:])
            if max_char != s_list[index]:
                for i in range(len(s_list) - 1, index - 1, -1):
                    if s_list[i] == max_char:
                        # Swap only if needed
                        if i != index:
                            s_list[index], s_list[i] = s_list[i], s_list[index]
                            candidate = ''.join(s_list)
                            if candidate > self.max_num:
                                self.max_num = candidate
                            helper(s_list, k - 1, index + 1)
                            # Backtrack
                            s_list[index], s_list[i] = s_list[i], s_list[index]
            else:
                helper(s_list, k, index + 1)

        helper(list(s), k, 0)
        return self.max_num


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        k = int(input())
        s = input()
        ob = Solution()
        print(ob.findMaximumNum(s, k))

        print("~")

# } Driver Code Ends