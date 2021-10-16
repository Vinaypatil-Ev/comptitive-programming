def is_rotate(s1, s2) -> bool:
    if len(s1) != len(s2):
        return False
    s: str = s1 + s1
    if s.count(s2) > 0:
        return True
    return False

if __name__ == "__main__":
    s1 = "ABCDE"
    s2 = "DEABC"
    isornot = "is" if is_rotate(s1, s2) else "is not"
    isornot += " rotation of"
    print(f"{s1} {isornot} {s2}")