def pf(no):
    """
    trivial division method
    O(root(n) * times of divison)
    """
    i = 2
    d = {}
    while i * i <= no:
        while no % i == 0:
            if i in d:
                d[i] += 1
            elif i not in d:
                d[i] = 1
            no //= i
        i += 1
    if no > 1:
        d[no] = 1
    return d

def pf2(no):
    """
    wheel factorization this is optimization of trivial divison
    O(root(n) * times of divison)
    if no / even no == 0:
        no / 2
    except 2 there is no prime no which even no
    """
    d = {}
    i = 2 # check all even no
    while no % i == 0:
        if i in d:
            d[i] += 1
        elif i not in d:
            d[i] = 1
        no //= i
    i = 3 # all the odd no
    while i * i <= no:
        while no % i == 0:
            if i in d:
                d[i] += 1
            elif i not in d:
                d[i] = 1
            no //= i
        i += 2

    if no > 1:
        d[no] = 1
    return d

def pf3(no):
    """
    wheel factorization this is optimization of trivial divison
    O(root(n) * times of divison)
    if no / even no == 0:
        no / 2
    except 2 there is no prime no which even no
    except 3 all the prime no are prime no
    """
    d = {}
    i = 2 # check all even no
    for i in [2, 3, 5]:
        while no % i == 0:
            if i in d:
                d[i] += 1
            elif i not in d:
                d[i] = 1
            no //= i
            
    i = 7 # all the odd no
    incp = [4, 2, 4, 2, 4, 6, 2, 6]
    inc = 0
    while i * i <= no:
        while no % i == 0:
            if i in d:
                d[i] += 1
            elif i not in d:
                d[i] = 1
            no //= i
        # inc = inc % 8
        if inc == 8:
            inc = 0
        i += incp[inc]

    if no > 1:
        d[no] = 1
    return d

def pf(no):
    """
    precomputed prime factorization
    list of prime no
    """
if __name__ == "__main__":
    d = pf3(int(input()))
    for k, v in d.items():
        print(k, v, end=" ")