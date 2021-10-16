def table(no, upto):
    if upto > 0:
        table(no, upto - 1)
        print(no * upto)



if __name__ == "__main__":
    table(2, 10)