def update(x, c=1):
    if c == 6:
        return
    print(x)
    update(x + f" {c}", c+1)
    update(x, c + 1)
    print(x)


x = "vinay: "
update(x)
print(x)