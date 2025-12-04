# Carson Wordekemper 12-3-25
# Lab 11 - This script reverses a string iteratively and recursively

def main():
    s = input("Enter a string: ")

    reverseIterativeResult = reverseIterative(s)
    print("Iterative:", reverseIterativeResult)

    reverseRecursiveResult = reverseRecursive(s)
    print("Recursive:", reverseRecursiveResult)

def reverseIterative(s):
    reversedS = ""
    for i in range(len(s)-1, -1, -1):
        reversedS += s[i]
    return reversedS

def reverseRecursive(s):
    if len(s) <= 1:
        return s
    return reverseRecursive(s[1:]) + s[0]

if __name__ == "__main__":
    main()