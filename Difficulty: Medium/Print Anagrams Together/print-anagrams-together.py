#User function Template for python3


class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        hashmap = {}
        
        for i in range(len(arr)):
            stri = sorted(arr[i])
            ele = ",".join(stri)
            # if ele not in hashmap:
            #     hashmap[ele] = []    
            # hashmap[ele].append(arr[i])
            hashmap.setdefault(ele,[]).append(arr[i])
            
        return [x for x in hashmap.values()]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        words = input().split()

        ob = Solution()
        ans = ob.anagrams(words)

        for grp in sorted(ans):
            for word in grp:
                print(word, end=' ')
            print()

        print("~")

# } Driver Code Ends