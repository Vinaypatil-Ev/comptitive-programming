#print solid rect

def solid_rectangle(l, h):
    for i in range(h):
        for j in range(l):
            print("*", end="")
        print()

# print how hollow rectangle

def hollow_rectangle(l, h):
    for i in range(1, h+1):
        for j in range(1, l+1):
            if j in {1, l} or i in {1, h}:
                print("*", end="")
            else:
                print(end=" ")
        print()

# pyramid printing
# half pyramid
def half_pyramid(h):
    for i in range(1, h+1):
        for j in range(i):
            print("*", end="")   
        print()   

# inverted half pyramid
def inverted_half_pyramid(h):
    for i in range(h, -1, -1):
        for j in range(i):
            print("*", end="")
        print()

# inverted hollow half pyrmaid       
def inverted_half_hollow_pyramid(h):
    for i in range(h, -1, -1):
        for j in range(i):
            if j in {0, i-1} or i in {0, h}:
                print("*", end="")
            else:
                print(end=" ")
        print()

# full pyramid

def full_pyramid(h):
    for i in range(h, 0, -1):
        for j in range(1, h*2-i+1):
            if j >= i:
                print("*", end="")
            else:
                print(end=" ")
        print()
        
def full_inverted_pyramid(h):
    for i in range(h):
        for j in range(0, h*2-i):
            if j > i:
                print("*", end="")
            else:
                print(end=" ")
        print()

        
def full_hollow_pyramid(h):
    for i in range(h, 0, -1):
        for j in range(1, h*2-i+1):
            if j in {i, 2 * h - i} or i == 1:
                print("*", end="")
            else:
                print(end=" ")
        print()
        
def half_pyramid_with_no(h):
    for i in range(1, h+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
    
def half_inverted_pyramid_with_no(h):
    for i in range(h, -1, -1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

def half_hollow_pyramid_with_no(h):
    for i in range(1, h+1):
        for j in range(1, i+1):
            if i == 1 or i == h or j == 1 or j == i:
                print(j, end="")
            else:
                print(end=" ")
        print()
                


if __name__ == "__main__":
    height = 5
    length = 5
    # solid_rectangle(length, height)
    # hollow_rectangle(length, height)
    # half_pyramid(height)
    # inverted_half_pyramid(height)
    # inverted_half_hollow_pyramid(height)
    full_pyramid(height)
    # full_inverted_pyramid(height)
    # full_hollow_pyramid(height)
    # half_pyramid_with_no(height)
    # half_inverted_pyramid_with_no(height)
    half_hollow_pyramid_with_no(height)
    

