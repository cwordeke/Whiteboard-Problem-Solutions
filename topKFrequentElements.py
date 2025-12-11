def main():
    test1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    result1 = topKFrequent(test1, k1)
    print("Return:", result1, "(Should Be: [1, 2])\n")
    
    test2 = [4, 1, 1, 1, 2, 2, 3]
    k2 = 2
    result2 = topKFrequent(test2, k2)
    print("Return:", result2, "(Should Be: [1, 2])\n")
    
    test3 = [1]
    k3 = 1
    result3 = topKFrequent(test3, k3)
    print("Return:", result3, "(Should Be: [1])\n")

def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    arr = []
    for num, cnt in count.items():
        arr.append([cnt, num])
    arr.sort()

    res = []
    while len(res) < k:
        res.append(arr.pop()[1])
    return res

if __name__ == "__main__":
    main()