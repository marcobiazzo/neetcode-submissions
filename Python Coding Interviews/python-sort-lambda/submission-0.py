from typing import List


def sort_words(words: List[str]) -> List[str]:
    get_word_length = lambda word: len(word)
    for j in range(len(words)):
        for i in range(len(words)):
            if i == len(words) - 1: break
            if get_word_length(words[i]) < get_word_length(words[i+1]):
                words[i], words[i+1] = words[i+1], words[i]

    return(words)


def sort_numbers(numbers: List[int]) -> List[int]:
    get_absolute_value = lambda number: abs(number)
    for j in range(len(numbers)):
        for i in range(len(numbers)):
            if i == len(numbers) - 1: break
            if get_absolute_value(numbers[i]) > get_absolute_value(numbers[i+1]):
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

    return(numbers)


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
