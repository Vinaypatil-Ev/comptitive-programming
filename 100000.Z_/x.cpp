#include<iostream>
#include<vector>

using namespace std;


template<class Iter>
void func(Iter start, Iter end) {}

int main() {
    int arr[10] = {1, 2, 3, 4, 5};
    // func(arr, arr + 5);        // first five elements
    // func(arr + 5, arr + 10);   // last five elements

    // std::vector<int> vec = {1, 2, 3, 4, 5, 5, 6, 7};
    // func(vec.begin(), vec.end());       // whole vector
    // func(vec.begin(), vec.begin() + 5); // first five elements
    // func(vec.begin() + 5, vec.end());   // all but the first five elements

    return 0;
}