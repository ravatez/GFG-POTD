#User function Template for python3


class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here
               
        sAlpha,pAlpha = [0]*26,[0]*26
        ct1 = ct2 = ind = 0
        
        mn = float('inf')
        res = ''
        
        for idx in p: 
            pAlpha[ord(idx)-97]+=1
            if pAlpha[ord(idx)-97] == 1: ct1+=1
            
        for l,(idx) in enumerate(s): 
            sAlpha[ord(idx)-97]+=1
            
            if sAlpha[ord(idx)-97] == pAlpha[ord(idx)-97]: ct2+=1
            
            if ct1 == ct2:
                
                while sAlpha[ord(s[ind])-97] > pAlpha[ord(s[ind])-97]: 
                    sAlpha[ord(s[ind])-97]-=1
                    ind += 1
                    
                if mn > (l - ind + 1):
                    mn = (l - ind + 1)
                    res = s[ind:l+1]
                
        return res if mn != float('inf') else '-1'

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends