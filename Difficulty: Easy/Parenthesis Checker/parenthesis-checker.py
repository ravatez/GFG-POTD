
class Solution:
    def isBalanced(self, s):
        # code here
        # code here

        n = len(s)

        stack = []

        for i in range(n):

            curr = s[i]

            if curr == '(' or curr == '{' or curr == '[':

                stack.append(curr)

            else:

                if not stack:

                    return False

                else:

                    top = stack[-1]

                    stack.pop()

                    if (curr == ')' and top != '(') or (curr == '}' and top != '{') or (curr == ']' and top != '['):

                        return False

        return True if len(stack) == 0 else False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s = str(input())
        obj = Solution()
        if obj.isBalanced(s):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends