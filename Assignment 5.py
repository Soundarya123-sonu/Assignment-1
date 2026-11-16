#1. Find the second-largest unique element in an array without using sort() or max().

# def second_largest(arr):
#     first = second = float('-inf')

#     for num in arr:
#         if num > first:
#             second = first
#             first = num
#         elif first > num > second:
#             second = num

#     if second == float('-inf'):
#         return "Second largest does not exist"

#     return second


# arr = [10, 20, 40, 30, 40, 50]
# print("Second Largest =", second_largest(arr))



#2. Find all pairs in an array whose sum equals a given target.
# def find_pairs(arr, target):
#     seen = set()
#     pairs = []

#     for num in arr:
#         required = target - num

#         if required in seen:
#             pairs.append((required, num))

#         seen.add(num)

#     return pairs


# arr = [2, 4, 3, 5, 7, 8, 1]
# target = 9

# print("Pairs =", find_pairs(arr, target))

#3. Move all zeros to the end of an array without changing the order of other elements.

# def move_zeros(arr):
#     result = []

#     for num in arr:
#         if num != 0:
#             result.append(num)

#     zero_count = len(arr) - len(result)

#     result.extend([0] * zero_count)

#     return result


# arr = [0, 1, 0, 3, 12, 0, 5]

# print("Result =", move_zeros(arr))

#4. Find the missing number from an array containing numbers from 1 to N.
# def missing_numbers(arr,n):
#     total = n * (n+1) // 2
#     actual_sum = sum (arr)
#     return  total - actual_sum
# arr = [1,2,3,4,5]
# n = 6
# print("Missing numbers =",missing_numbers(arr,n))


#5. Find all duplicate elements in a list without using nested loops.
# def find_duplicates(arr):
#     seen = set()
#     duplicates = set()

#     for num in arr:
#         if num in seen:
#             duplicates.add(num)
#         else:
#             seen.add(num)

#     return list(duplicates)


# arr = [1, 2, 3, 2, 4, 5, 3, 6]

# print("Duplicates =", find_duplicates(arr))


#6. Find the first non-repeating character in a string.
# def first_non_repeating(text):
#     frequency = {}

#     for char in text:
#         frequency[char] = frequency.get(char, 0) + 1

#     for char in text:
#         if frequency[char] == 1:
#             return char

#     return "No non-repeating character"


# text = "swiss"

# print("First Non-Repeating =", first_non_repeating(text))


#7. Check whether two strings are anagrams without using sorted().

# def are_anagrams(str1, str2):
#     if len(str1) != len(str2):
#         return False

#     frequency = {}

#     for char in str1:
#         frequency[char] = frequency.get(char, 0) + 1

#     for char in str2:
#         if char not in frequency:
#             return False

#         frequency[char] -= 1

#         if frequency[char] < 0:
#             return False

#     return True


# str1 = "listen"
# str2 = "silent"

# if are_anagrams(str1, str2):
#     print("Strings are Anagrams")
# else:
#     print("Strings are not Anagrams")


#8. Merge two sorted arrays without using sort().
# def merge_arrays(arr1, arr2):
#     i = 0
#     j = 0
#     result = []

#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             result.append(arr1[i])
#             i += 1
#         else:
#             result.append(arr2[j])
#             j += 1

#     result.extend(arr1[i:])
#     result.extend(arr2[j:])

#     return result


# arr1 = [1, 3, 5, 7]
# arr2 = [2, 4, 6, 8]

# print("Merged Array =", merge_arrays(arr1, arr2))


#9. Rotate an array to the right by K positions.
# def rotate_array(arr,k):
#     if len(arr) == 0:
#         return arr
#     k = k % len(arr)
#     return arr[-k:] + arr[:-k] if k != 0 else arr
# arr = [1,2,3,4,5]
# k = 3
# print("Rotated Array =", rotate_array(arr, k))


#10. Find the intersection of two arrays, including duplicate occurrences.
# def intersection(arr1, arr2):
#     frequency = {}

#     for num in arr1:
#         frequency[num] = frequency.get(num, 0) + 1

#     result = []

#     for num in arr2:
#         if frequency.get(num, 0) > 0:
#             result.append(num)
#             frequency[num] -= 1

#     return result


# arr1 = [1, 2, 2, 3, 4]
# arr2 = [2, 2, 3, 5]

# print("Intersection =", intersection(arr1, arr2))


#11. Find the maximum sum of a contiguous subarray.
# def max_subarray_sum(arr):
#     current_sum = arr[0]
#     max_sum = arr[0]

#     for num in arr[1:]:
#         current_sum = max(num, current_sum + num)
#         max_sum = max(max_sum, current_sum)

#     return max_sum


# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# print("Maximum Subarray Sum =", max_subarray_sum(arr))


#12. Find the longest substring without repeating characters.
# def longest_substring(text):
#     seen = {}
#     start = 0
#     max_length = 0
#     result = ""

#     for end in range(len(text)):
#         char = text[end]

#         if char in seen and seen[char] >= start:
#             start = seen[char] + 1

#         seen[char] = end

#         if end - start + 1 > max_length:
#             max_length = end - start + 1
#             result = text[start:end + 1]

#     return result


# text = "MOMOMOMO"

# print("Longest Substring =", longest_substring(text))

#13. Find the longest common prefix among multiple strings.

# words = ["flower", "flow", "flight"]

# prefix = words[0]

# for word in words:
#     while not word.startswith(prefix):
#         prefix = prefix[:-1]

# print("Longest Common Prefix =", prefix)

#14. Group a list of strings into anagram groups.

# words = ["ate","eat","tea","nat","bat"]
# groups = {}
# for word in words:
#     key = "".join(sorted(word))
#     if key not in groups:
#         groups[key] = []

#     groups[key].append(word)

# print(list(groups.values()))

#15. Find the Kth largest element in an unsorted array.
# numbers = [3, 2, 1, 5, 6, 4]
# k = 2
# numbers.sort(reverse = True)
# print("Kth Largest Element =", numbers[k - 1])

#16. Check whether a given string contains balanced parentheses using a stack.
# text = "{[()]}"

# stack = []
# balanced = True

# for char in text:
#     if char in "({[":
#         stack.append(char)

#     elif char in ")}]":
#         if len(stack) == 0:
#             balanced = False
#             break

#         top = stack.pop()

#         if (char == ")" and top != "(") or \
#            (char == "}" and top != "{") or \
#            (char == "]" and top != "["):
#             balanced = False
#             break

# if len(stack) != 0:
#     balanced = False

# if balanced:
#     print("Balanced Parentheses")
# else:
#     print("Not Balanced Parentheses")

#17. Find all subarrays whose sum equals a given target.
# numbers = [1,2,3,4,2]
# target = 5
# for i in range(len(numbers)):
#     total = 0
#     for j in range(i,len(numbers)):
#         total = total + numbers[j]

#         if total == target:
#             print(numbers[i:j+1])

#18. Merge overlapping intervals in a list.

# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

# intervals.sort()
# result = []

# for i in intervals:
#     if not result or result[-1][1] < i[0]:
#         result.append(i)
#     else:
#         result[-1][1] = max(result[-1][1], i[1])

# print(result)

