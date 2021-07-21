# prime no
def is_prime(n):
    if n <= 1:
        return False
    if n in {2, 3}:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# palindrome no
def is_palindrome(n):
    temp = n
    no = 0
    while temp != 0:
        no = no * 10 + temp % 10
        temp = temp // 10
    if no == n:
        return True
    return False

def is_armstrong(n):
    temp = n
    no = 0
    while temp != 0:
        t = temp % 10
        no += t * t * t
        temp = temp // 10
    if no == n:
        return True
    return False


        

if __name__ == "__main__":
    print("is 11 prime:", is_prime(11))
    print("is 121 palindrome no:", is_palindrome(121))
    print("is 153 armstrong no: ", is_armstrong(153))