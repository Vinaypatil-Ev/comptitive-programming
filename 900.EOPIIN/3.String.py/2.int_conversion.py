
def stoi(s):
    no = 0
    flag = False
    if s[0] == "-":
        s = s[1:]
        flag = True
    for i in s:
        no = no * 10 + (ord(f"{i}")+2)%10
    return no if not flag else -no
    
def itos(no):
    if no != 0:
        # no = 0
        itos(no//10)
        x = print(no)
        print(x)
        

if __name__ == "__main__":
    # s = "-32423"
    # print(stoi(s))
    print(itos(455))

    