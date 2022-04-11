#include<bits/stdc++.h>
using namespace std;

int solution(int n) {
    int steps = 0;
    int x = 32768;
    while (x != n) {
        if (((x % 2) == 0) and ((x / 2) > n)) {
            x /= 2;
        }else x--;
        steps++;
    }
    return steps;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        cout << solution(n) << " ";
    }
}