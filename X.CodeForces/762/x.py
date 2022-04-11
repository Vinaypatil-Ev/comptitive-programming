def pythogorialTriplets(n):
    c, m = 0, 2
    count = 0
    while c < n:
        for i in range(1, m):
            a = m * m - i * i
            b = 2 * m * i
            c = m * m + i * i 
            count += 1

            # if c > n:
            #     break

            print(a, b, c) # this line print the triplet 

        m = m + 1  
    return count      # It will return the Count or no of Triplets.   

if __name__ == "__main__":
    n = int(input())
    print(pythogorialTriplets(n))