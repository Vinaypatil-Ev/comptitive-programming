#include<bits/stdc++.h>
using namespace std;

long long minSum(int n, vector<int> &a, vector<int> &b) {
    long long msa = 0, msb = 0;
    int i = 1;
    while (i < n) {
        int x = abs(a[i - 1] - a[i]);
        int y = abs(b[i - 1] - b[i]);
        int xx = abs(a[i - 1] - b[i]);
        int yy = abs(abs(b[i - 1] - a[i]));
        if (x + y < xx + yy) {
            msa += x;
            msb += y;
        }else {
            msa += xx;
            msb += yy;
        }
        
        i++;
    }
    return msa + msb;
}
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, x;
        vector<int> a, b;
        cin >> n;
        for (int i= 0; i < n; i++) {
            cin >> x;
            a.push_back(x);
        }
        for (int i=0; i < n; i++) {
            cin >> x;
            b.push_back(x);
        }
        cout << minSum(n, a, b) << endl;
    }
    return 0;
}