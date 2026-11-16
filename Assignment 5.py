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

#19. Search for an element in a rotated sorted array.

# arr = [4, 5, 6, 7, 0, 1, 2]
# target = 0

# left = 0
# right = len(arr) - 1

# while left <= right:
#     mid = (left + right) // 2

#     if arr[mid] == target:
#         print("Found at index:", mid)
#         break
#     elif arr[left] <= arr[mid]:
#         if arr[left] <= target < arr[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1
#     else:
#         if arr[mid] < target <= arr[right]:
#             left = mid + 1
#         else:
#             right = mid - 1
# else:
#     print("Not found")


#20. Find the longest consecutive sequence in an unsorted array.

# arr = [100,4,200,1,2,3,4]

# s = set(arr)
# longest = 0
# for i in s:
#     if i - 1 not in s:
#         count = 1
#         num = i
#         while num -1 in s:
#             num -- 1
#             count -- 1
#             longest = max(longest.count)

# print(longest)


#21. Find the trapped rainwater between elevation bars.

# arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# left = 0
# right = len(arr) - 1

# left_max = 0
# right_max = 0
# water = 0

# while left <= right:
#     if arr[left] < arr[right]:
#         if arr[left] >= left_max:
#             left_max = arr[left]
#         else:
#             water += left_max - arr[left]
#         left += 1
#     else:
#         if arr[right] >= right_max:
#             right_max = arr[right]
#         else:
#             water += right_max - arr[right]
#         right -= 1

# print(water)


#22. Find the median of two sorted arrays in O(log(m+n)) time.

# a = [1,3]
# b =[2]
# arr = sorted(a + b)
# n = len(arr)
# if n % 2 == 1:
#     median = arr[n // 2]
# else:
#     median = (arr[n // 2 -1] + arr[n // 2]) / 2

# print(median)   



#23. Find the maximum product of a contiguous subarray.

# arr = [2,3,-2,4]
# maximum = arr[0]
# minimum = arr[0]
# result = arr[0]

# for i in arr[1:]:
#     if i < 0:
#         maximum, minimum = minimum, maximum

#     maximum = max(i,maximum *i)
#     minimum = min(i,minimum*i)

#     result = max(result,maximum)
# print(result)



#24. Find the smallest missing positive integer from an unsorted array.

# arr = [3,4,-1,1]
# num = 1
# while num in arr:
#     num += 1
# print(num)  


#25. Count the number of subarrays whose sum equals K.

# arr = [1,2,3]
# k = 3
# count = 0
# for i in range(len(arr)):
#     total = 0
#     for j in range(i,len(arr)):
#         total += arr[j]
#         if total == k:
#             count += 1

# print(count) 



#26. Find the longest increasing subsequence in an array.

# arr = [10, 9, 2, 5, 3, 7, 101, 18]

# dp = [1]* len (arr)
# for i in range(len(arr)):
#     for j in range(i):
#         if arr[i]> arr[j]:
#             dp[i] = max(dp[i],dp[j] + 1)
# print(max(dp))

#27. Solve the Coin Change problem using dynamic programming.

# coins = [1, 2, 5]
# amount = 11

# dp = [float('inf')] * (amount + 1)
# dp[0] = 0

# for i in range(1, amount + 1):
#     for coin in coins:
#         if coin <= i:
#             dp[i] = min(dp[i], dp[i - coin] + 1)

# if dp[amount] == float('inf'):
#     print(-1)
# else:
#     print(dp[amount])


#28. Solve the Word Break problem using dynamic programming.

# s = "leetcode"
# word = ["leet","code"]
# dp = [False] * (len(s) + 1)
# dp [0] = True
# for i in range(1, len(s) + 1):
#     for j in range(i):
#         if dp[j] and s[j:i] in word:
#             dp[i] = True
#             break

# print(dp[len(s)])


# 29. Find the minimum number of jumps required to reach the last index.

# arr = [2, 3, 1, 1, 4]
# jumps = 0
# current_end = 0
# farthest = 0
# for i in range(len(arr) - 1):
#     farthest = max(farthest, i + arr[i])

#     if i == current_end:
#         jumps += 1
#         current_end = farthest

# print(jumps)

#30. Find the maximum profit from buying and selling stocks with multiple transactions.

# prices = [7, 1, 5, 3, 6, 4]

# profit = 0

# for i in range(1, len(prices)):
#     if prices[i] > prices[i - 1]:
#         profit += prices[i] - prices[i - 1]

# print(profit)


#31. Implement an LRU Cache with O(1) time complexity for get() and put().

# from collections import OrderedDict

# class LRUCache:

#     def __init__(self, capacity):
#         self.cache = OrderedDict()
#         self.capacity = capacity

#     def get(self, key):
#         if key not in self.cache:
#             return -1

#         self.cache.move_to_end(key)
#         return self.cache[key]

#     def put(self, key, value):
#         if key in self.cache:
#             self.cache.move_to_end(key)

#         self.cache[key] = value

#         if len(self.cache) > self.capacity:
#             self.cache.popitem(last=False)


# obj = LRUCache(2)

# obj.put(1, 10)
# obj.put(2, 20)

# print(obj.get(1))

# obj.put(3, 30)

# print(obj.get(2))


#32. Implement a Min Stack that supports push(), pop(), top() and getMin() in O(1).

# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.min_stack = []

#     def push(self, x):
#         self.stack.append(x)

#         if not self.min_stack or x <= self.min_stack[-1]:
#             self.min_stack.append(x)

#     def pop(self):
#         x = self.stack.pop()

#         if x == self.min_stack[-1]:
#             self.min_stack.pop()

#     def top(self):
#         return self.stack[-1]

#     def getMin(self):
#         return self.min_stack[-1]


# s = MinStack()

# s.push(5)
# s.push(2)
# s.push(8)

# print(s.getMin())
# print(s.top())

#33. Find the number of islands in a 2D matrix using DFS or BFS.

# grid = [
#     ["1", "1", "0"],
#     ["1", "0", "0"],
#     ["0", "0", "1"]
# ]

# def dfs(i, j):
#     if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
#         return

#     if grid[i][j] == "0":
#         return

#     grid[i][j] = "0"

#     dfs(i + 1, j)
#     dfs(i - 1, j)
#     dfs(i, j + 1)
#     dfs(i, j - 1)


# count = 0

# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if grid[i][j] == "1":
#             dfs(i, j)
#             count += 1

# print(count)

#34. Find the shortest path in a weighted graph using Dijkstra's algorithm.

# import heapq

# graph = {
#     0: [(1, 4), (2, 1)],
#     1: [(3, 1)],
#     2: [(1, 2), (3, 5)],
#     3: []
# }

# dist = {i: float('inf') for i in graph}
# dist[0] = 0

# pq = [(0, 0)]

# while pq:
#     cost, node = heapq.heappop(pq)

#     if cost > dist[node]:
#         continue

#     for neighbour, weight in graph[node]:
#         new_cost = cost + weight

#         if new_cost < dist[neighbour]:
#             dist[neighbour] = new_cost
#             heapq.heappush(pq, (new_cost, neighbour))

# print(dist)

#35. Detect a cycle in a directed and undirected graph.

# graph = {
#     0: [1],
#     1: [0, 2],
#     2: [1, 0]
# }

# def dfs(node, parent, visited):
#     visited.add(node)

#     for neighbour in graph[node]:
#         if neighbour not in visited:
#             if dfs(neighbour, node, visited):
#                 return True
#         elif neighbour != parent:
#             return True

#     return False


# visited = set()
# print(dfs(0, -1, visited))


#36. Implement topological sorting for a directed acyclic graph.

# graph = {
#     0: [1, 2],
#     1: [3],
#     2: [3],
#     3: []
# }

# visited = set()
# stack = []

# def dfs(node):
#     visited.add(node)

#     for neighbour in graph[node]:
#         if neighbour not in visited:
#             dfs(neighbour)

#     stack.append(node)


# for node in graph:
#     if node not in visited:
#         dfs(node)

# print(stack[::-1])


#37. Solve the N-Queens problem using backtracking.
# def solve(n):
#     board = [["."] * n for i in range(n)]

#     def safe(row, col):
#         for i in range(row):
#             if board[i][col] == "Q":
#                 return False

#         i, j = row - 1, col - 1
#         while i >= 0 and j >= 0:
#             if board[i][j] == "Q":
#                 return False
#             i -= 1
#             j -= 1

#         i, j = row - 1, col + 1
#         while i >= 0 and j < n:
#             if board[i][j] == "Q":
#                 return False
#             i -= 1
#             j += 1

#         return True

#     def backtrack(row):
#         if row == n:
#             for r in board:
#                 print("".join(r))
#             return True

#         for col in range(n):
#             if safe(row, col):
#                 board[row][col] = "Q"

#                 if backtrack(row + 1):
#                     return True

#                 board[row][col] = "."

#         return False

#     backtrack(0)


# solve(4)

#38. Generate all permutations of a given string or array without duplicates.
# arr = [1, 2, 2]

# def permute(arr, path=[]):
#     if not arr:
#         print(path)
#         return

#     used = set()

#     for i in range(len(arr)):
#         if arr[i] not in used:
#             used.add(arr[i])
#             permute(arr[:i] + arr[i+1:], path + [arr[i]])


# permute(arr)

#39. Serialize and deserialize a binary tree.
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# def serialize(root):
#     if not root:
#         return "None"

#     return str(root.val) + "," + serialize(root.left) + "," + serialize(root.right)


# def deserialize(data):
#     values = iter(data.split(","))

#     def build():
#         val = next(values)

#         if val == "None":
#             return None

#         node = Node(int(val))
#         node.left = build()
#         node.right = build()

#         return node

#     return build()


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)

# data = serialize(root)
# print(data)

# new_root = deserialize(data)
# print(new_root.val)

#40. Find the lowest common ancestor of two nodes in a binary tree.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lca(root, p, q):
    if root is None or root == p or root == q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root

    return left if left else right


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

result = lca(root, root.left.left, root.left.right)

print(result.val)