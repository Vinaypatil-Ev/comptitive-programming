def urlify(s):
    s = s.split()
    return "%20".join(s)

def urlify(s):
    pass



if __name__ == "__main__":
    # s = "This is google yard"
    s = input()
    x = urlify(s)
    print(x)