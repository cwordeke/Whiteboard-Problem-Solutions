# Carson Wordekemper 12-3-25
# Lab 11 - This script completes two sum in 2 different ways

def main():
    intList = [1, 3, 6]
    target = 7

    twoSumLoopsResult = twoSumLoops(intList, target)
    print("twoSumLoops:", twoSumLoopsResult)

    twoSumDictResult = twoSumDict(intList, target)
    print("twoSumDict:", twoSumDictResult)

    twoSumLoopsAllResult = twoSumLoopsAll(intList, target)
    print("twoSumLoopsAll:", twoSumLoopsAllResult)

    twoSumDictAllResult = twoSumDictAll(intList, target)
    print("twoSumDictAll:", twoSumDictAllResult)

# Method 1
def twoSumLoops(intList, target):
    for i in range(len(intList)):
        for j in range(i + 1, len(intList)):
            if intList[i] + intList[j] == target:
                return i, j
            
# Method 2
def twoSumDict(intList, target):
    numToIndex = {}
    for i in range(len(intList)):
        complement = target - intList[i]

        if complement in numToIndex:
            return numToIndex[complement], i
        
        numToIndex[intList[i]] = i

# All possible index pairs
def twoSumLoopsAll(intList, target):
    allPairs = []
    for i in range(len(intList)):
        for j in range(i+1, len(intList)):
            if intList[i] + intList[j] == target:
                allPairs.append([i,j])
    return allPairs

def twoSumDictAll(intList, target):
    numToIndex = {}
    for i in range(len(intList)):
        complement = target - intList[i]

        if complement in numToIndex:
            return numToIndex[complement], i
        
        numToIndex[intList[i]] = i

if __name__ == "__main__":
    main()