#for reverse integer
def reverse(x: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    sign = -1 if x < 0 else 1
    reversed_str = str(abs(x))[::-1]
    reversed_int = sign * int(reversed_str)
    
    if reversed_int < INT_MIN or reversed_int > INT_MAX:
        return 0
    return reversed_int

#for fizz buzz
def fizzBuzz(n: int) -> list[str]:
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

#Number of Steps to Reduce a Number to Zero
def numberOfSteps(num: int) -> int:
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        steps += 1
    return steps

#Count Odd Numbers in an Interval Range
def countOdds(low: int, high: int) -> int:
    return (high - low) // 2 + (1 if low % 2 != 0 or high % 2 != 0 else 0)

#Add Digits
def addDigits(num: int) -> int:
    if num == 0:
        return 0
    return 1 + (num - 1) % 9

#Palindrome Number
def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]

#Factorial Trailing Zeroes
def trailingZeroes(n: int) -> int:
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

#Chapter 2 – Data Structures (List, Dict, Stack, Queue, etc.)
#Two Sum
def twoSum(nums: list[int], target: int) -> list[int]:
    num_map = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
#Valid Parentheses (Stack)
def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)

    return not stack
#Merge Two Sorted Lists
  #i couldn't do it :(

#Remove Duplicates from Sorted Array
def removeDuplicates(nums: list[int]) -> int:
    if not nums:
        return 0

    unique_index = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[unique_index] = nums[i]
            unique_index += 1
    
    return unique_index
#Contains Duplicate
def containsDuplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

#Intersection of Two Arrays II
from collections import Counter

def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    count1 = Counter(nums1)
    count2 = Counter(nums2)
    result = []
    
    for num in count1:
        if num in count2:
            result.extend([num] * min(count1[num], count2[num]))
    
    return result

#Maximum Number of Words Found in 
 #it says page not found

#Chapter 3 – Algorithms (Searching, Sorting, Recursion)
#Binary Search
def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

#Guess Number Higher or Lower
def guessNumber(m: int) -> int:
    low, high = 1, m
    
    while low <= high:
        mid = low + (high - low) // 2
        result = guess(mid)
        
        if result == 0:
            return mid
        elif result == -1:
            high = mid - 1
        else:
            low = mid + 1

#First Bad Version
def firstBadVersion(n: int) -> int:
    left, right = 1, n
    
    while left < right:
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

#Search Insert Position
def searchInsert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left

#Merge Sorted Array
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i, j, k = m - 1, n - 1, m + n - 1
    
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
#Climbing Stairs
def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    
    first, second = 1, 2
    
    for i in range(3, n + 1):
        first, second = second, first + second
    
    return second
    
#Fibonacci Number
def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    first, second = 0, 1
    
    for i in range(2, n + 1):
        first, second = second, first + second
    
    return second

