from typing import TypedDict


def get_word_count(contents: str) -> int:
    return len(contents.split())


def get_character_counts(contents: str) -> dict[str, int]:
    char_counts: dict[str, int] = {}
    contents_lower: str = contents.lower()
    for char in contents_lower:
        if not char in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    return char_counts


class CharCount(TypedDict):
    char: str
    num: int


def sort_on(char_dict: CharCount) -> int:
    return char_dict['num']


def sort_chars(char_counts: dict[str, int]) -> list[CharCount]:
    char_counts_list: list[CharCount] = []
    for char in char_counts:
        char_counts_list.append({"char": char, "num": char_counts[char]})
    char_counts_list.sort(reverse=True, key=sort_on)
    return char_counts_list
