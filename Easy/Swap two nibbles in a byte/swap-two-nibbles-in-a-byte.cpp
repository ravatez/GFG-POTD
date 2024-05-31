//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    int swapNibbles(int n)  {
    // Extract the two nibbles
    int firstNibble = (n & 0xF0) >> 4; // Extract the first nibble (higher 4 bits)
    int secondNibble = (n & 0x0F); // Extract the second nibble (lower 4 bits)
    
    // Swap the nibbles
    int swappedNibbles = (secondNibble << 4) | firstNibble;
    
    return swappedNibbles;
}
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        Solution ob;
        cout << ob.swapNibbles(n) << endl;
    }
    return 0;
}
// } Driver Code Ends