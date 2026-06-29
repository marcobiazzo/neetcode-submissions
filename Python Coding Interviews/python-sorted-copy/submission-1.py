from typing import List


def sort_words(words: List[str]) -> List[str]:
    words_ordered = words
    for j in range(len(words_ordered)):
        for i in range(len(words_ordered)):
            if i == len(words_ordered) - 1: break
            if words_ordered[i] > words_ordered[i+1]:
                words_ordered[i], words_ordered[i+1] = words_ordered[i+1], words_ordered[i]

    return(words_ordered)


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers_ordered = numbers
    for j in range(len(numbers_ordered)):
        for i in range(len(numbers_ordered)):
            if i == len(numbers_ordered) - 1: break
            if abs(numbers_ordered[i]) < abs(numbers_ordered[i+1]):
                numbers_ordered[i], numbers_ordered[i+1] = numbers_ordered[i+1], numbers_ordered[i]

    return(numbers_ordered)


# do not modify below this line
original_words = ["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]

print(original_words)
print(sort_words(original_words))

original_numbers = [1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]

print(original_numbers)
print(sort_numbers(original_numbers))
