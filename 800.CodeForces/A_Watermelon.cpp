#include<iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    if (n != 2 && n % 2 == 0){
        cout << "YES";
    }else {
        cout << "NO";
        bool x = n & 1 != 0;
    }
}