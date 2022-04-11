def solution(s):
    # green
    n = len(s)
    if n <= 1:
        return 0
    zeros = s.count("0")
    ones = s.count("1")
    print(zeros, ones)
    if ones == zeros: return 0
    if zeros < ones:
        s = s.replace("0", "")
    else:
        s = s.replace("1", "")
    return n - len(s)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        # solution(input())
        print(solution(input()))