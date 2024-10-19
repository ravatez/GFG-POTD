#User function Template for python3

import sys
sys.set_int_max_str_digits(0)
class Solution:
    def roundToNearest (self, Str) : 
        last_digit=int(Str)%10
        last_digit_minus_10=10-last_digit
        Ans=""
        i=0
        while Str[i]=='0':
            Ans+='0'
            i+=1
                
        if last_digit_minus_10>=last_digit:
            Nearest_Multiple=Ans+str(int(Str)-last_digit)
            return Nearest_Multiple
        Nearest_Multiple=Ans+str(int(Str)+last_digit_minus_10)
        return Nearest_Multiple



#{ 
 # Driver Code Starts
#Initial Template for Python 3
for _ in range(0, int(input())):
    num_str = input()
    ob = Solution()
    res = ob.roundToNearest(num_str)
    print(res)

# } Driver Code Ends