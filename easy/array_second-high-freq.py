# [1, 3, 5, 6, 7, 2, 3, 5, 3]


def findSecondHighestFreq(arr):
    if len(arr) < 2:
        return None

    dictionary = {}
    for num in arr:
        if num in dictionary:
            dictionary[num] += 1
        else:
            dictionary[num] = 1

    highestFreq = 0
    numHighestFreq = None
    secondHighest = 0
    numSecondHighest = None
    for key in dictionary:
        if dictionary[key] > highestFreq:
            highestFreq = dictionary[key]
            numHighestFreq = key
        elif dictionary[key] > secondHighest:
            secondHighest = dictionary[key]
            numSecondHighest = key

    if highestFreq == secondHighest:
        return numHighestFreq

    return numSecondHighest


print(findSecondHighestFreq([1, 3, 5, 6, 7, 2, 3, 5, 3]))
