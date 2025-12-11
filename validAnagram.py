def main():
    test1 = ("listen", "silent")
    result1 = isAnagram(test1[0], test1[1])
    print("Return:", result1, "(Should Be: True)\n")
    
    test2 = ("hello", "world")
    result2 = isAnagram(test2[0], test2[1])
    print("Return:", result2, "(Should Be: False)\n")
    
    test3 = ("a", "a")
    result3 = isAnagram(test3[0], test3[1])
    print("Return:", result3, "(Should Be: True)\n")

def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

if __name__ == "__main__":
    main()