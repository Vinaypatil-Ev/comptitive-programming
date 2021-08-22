#include<iostream>
using namespace std;
void print(int *arr, int n) {
    if (n >= 0) {
        cout << *(arr + n) << " ";
        print(arr, n - 1);
    }
}
void print_r(int *arr, int n) {
    if (n >= 0) {
        print_r(arr, n - 1);
        cout << arr[n] << " ";
    }
}

int main() {
    int arr[] = {100, 200, 300, 400, 500, 600, 700, 800, 900};
    int n = sizeof(arr) / sizeof(int); // int * n
    print(arr, n - 1);
    cout << endl;
    print_r(arr, n - 1);
    cout << endl;
}