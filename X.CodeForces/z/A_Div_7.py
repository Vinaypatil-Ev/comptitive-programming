def solution(n):
    if n % 7 == 0: return n
    
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(solution(int(input())))