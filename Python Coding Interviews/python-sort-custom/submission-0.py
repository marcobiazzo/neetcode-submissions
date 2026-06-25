from typing import List


def sort_words(words: List[str]) -> List[str]:
    for j in range(len(words)):
        for i in range(len(words)):
            if i == len(words) - 1: break
            if len(words[i]) < len(words[i+1]):
                words[i], words[i+1] = words[i+1], words[i]

    return(words)


def sort_numbers(numbers: List[int]) -> List[int]:
    for j in range(len(numbers)):
        for i in range(len(numbers)):
            if i == len(numbers) - 1: break
            if abs(numbers[i]) > abs(numbers[i+1]):
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

    return(numbers)


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
