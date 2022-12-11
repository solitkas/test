from typing import List

listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]


def findMissingNumbers(n: List[int]) -> List[int]:
    """
    To find the missing number in an array
    """
    numbers = set(n)
    a, b = min(numbers), max(numbers)
    output = []
    for i in range(a, b):
        if i not in numbers:
            output.append(i)
    return output


if __name__ == "__main__":
    print(findMissingNumbers(listOfNumbers))


