#include<iostream>
#include<vector>

using namespace std;


int main() {
    int a[2][2] = {1, 2, 3, 4};
    cout << *(int*)a << endl;
    cout << (int*)a << endl;
    cout << *a << endl;
    cout << *(int*)a + 1 << endl;
    cout << (int*)a + 2 << endl;
    cout << (int*)a + 3 << endl;
    return 0;
}