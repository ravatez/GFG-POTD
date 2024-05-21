//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++

class Solution {
  public:
    vector<int> printKClosest(vector<int> arr, int n, int k, int x) {
        // code here
        int left=0,right=n-1,index=0,nearest=0;
       while(left<=right){
            int mid=left+(right-left)/2;
            if(abs(nearest-x)>abs(arr[mid]-x)) nearest=arr[mid],index=mid;
            if(abs(nearest-x)==abs(arr[mid]-x))if(arr[mid]>nearest) index=mid,nearest=arr[mid];
            if(arr[mid]>x) right=mid-1;
            else left=mid+1;
        }
        left=nearest!=x?index:index-1;
        right=index+1;
        vector<int>closest;
        while(k&&left>=0&&right<n)
        closest.push_back(abs(arr[left]-x)<abs(arr[right]-x)?arr[left--]:arr[right++]),k--;
        while(left>=0&&k) closest.push_back(arr[left--]),k--;
        while(right<n&&k) closest.push_back(arr[right++]),k--;
        return closest;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, k, x;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        cin >> k >> x;
        Solution ob;
        auto ans = ob.printKClosest(arr, n, k, x);
        for (auto e : ans) {
            cout << e << " ";
        }
        cout << "\n";
    }
    return 0;
}

// } Driver Code Ends