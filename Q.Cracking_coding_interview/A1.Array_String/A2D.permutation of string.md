# Permutation of string

### 1.How to generate permuations of string

To generate permution of string, we need to swap each character in the string with every other character in string. To do so, create function name permute, take index of current element as one of the argument to the function and swap the current element with every other element in the string and recurse that string with next index of current index. while returning back from recursion, we reverse the swaping done in the current function call.

```py
def swap(s, x, y):
    s[x], s[y] = s[y], s[x]

def generate_permuation(s, left, right):
    if left < right:
        for i in range(left, right+1):
            swap(s, left, i)
            generate_permuation(s, left+1, right)
            swap(s, left, i)
    if left == right:
        print("".join(s))


if __name__ == "__main__":
    s = "abc"
    s = list(s)
    generate_permuation(s, 0, len(s) - 1)
```

Time complexity - O(n!)

Space complexity - O(n^2)

### 2.Given two strings, write a method to decide if one is a permutation of the other

Note - length of both strings should be equal else return False

##### 1.Permution: Generate all the permation of first string and check wether it second string

##### 2.Sorting: sort both string and compare both strings - O(nlogn)

##### 3.Hash map and Array[26]: Calculate frequecies of each each character in both string and store it into hashmap/Array[26] and compare these hashmaps/Array if they are eqal then return True - O(n)
