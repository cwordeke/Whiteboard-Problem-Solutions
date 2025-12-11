def main():
    test1 = [1, 2, 3, 4, 2, 5]
    result1 = hasDuplicate(test1)
    print("Return:", result1, "(Should Be: True)\n")
    
    test2 = [1, 2, 3, 4, 5]
    result2 = hasDuplicate(test2)
    print("Return:", result2, "(Should Be: False)\n")
    
    test3 = [1]
    result3 = hasDuplicate(test3)
    print("Return:", result3, "(Should Be: False)\n")

def hasDuplicate(nums: list[int]) -> bool:
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] == nums[j]):
                return True
    return False

if __name__ == "__main__":
    main()