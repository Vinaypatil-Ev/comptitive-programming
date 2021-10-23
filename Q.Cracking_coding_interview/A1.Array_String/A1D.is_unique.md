# Is unique

Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

1.HashMap Approach (using datastructure

```py
def is_unique(s):
    d = set()
    for i in s:
        if i not in d:
            d.add(i)
        elif i in d:
            return False
    return True
```

### 2.Bit array

First calculate the ASCII value of the character and store it into ith varible. Now set the bit at ith position. if bit is aleardy set then that character is repeate hence return False and if you do not found any set bit then return False

```py
def is_unique(s):
    bit_arr = 0
    a = ord("a")
    for i in s:
        ith = ord(i) - a
        if bit_arr & (1 << ith):
            return False
        bit_arr |= (1 << ith)
    return True
```
