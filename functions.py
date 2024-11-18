# TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    lst[::-1]
    return lst
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    pass  # Implement this

def count_occurrences(lst, element):
    count = 0
    for i in lst:
        if element == lst[i]:
            count += 1
    return count

    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    pass  # Implement this

def get_keys_with_value(dct, value):
    for value in {dct,value}:
        if value in {dct,value}:
            return dct
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    pass  # Implement this

def merge_sorted_lists(lst1, lst2):
    final = lst1.append(lst2)
    return final
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    pass  # Implement this

def find_second_largest(numbers):
    lst = []
    largest = max(numbers)
    lst.append(largest)
    # return max(numbers)
    print(numbers)
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    pass  # Implement this

def is_anagram(str1, str2):
    ana = []
    if len(str1) != len(str2):
        return False
    for i in str1:
        if i in str2:
            ana.append(i)
        if len(ana) == len(str2):
            return True
    # count= len(str1)
    # for i in str1:
    #     if i in str2:
    #         str1.remove(i)
    #         count -=1
    # if count > 0:
    #     return False
    else:
        return True

    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    pass  # Implement this


def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    pass  # Implement this


def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    pass  # Implement this

def find_common_elements(lst1, lst2):
    common = []
    for i in lst1:
        if i in lst2:
            common.append(i)

    return common
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    pass  # Implement this



print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))