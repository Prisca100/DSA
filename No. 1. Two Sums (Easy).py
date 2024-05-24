"""Arrays and Hash Maps"""

# Brute force
# Time complexity : O(n^2)
# Space complexity = O(n)
def two_sum(nums, target):
    for i in range(len(nums)-1):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return [(str(i), nums[i]), (str(j), nums[j])]
    return []

# Optimization using memoization with a hashmap (dictionary)
# Time complexity = O(n)
# Space complexity = O(n)
def two_sums_optimized(nums, target):
    solution_dict = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in solution_dict:
            return [solution_dict[complement], i]
        solution_dict[nums[i]] = i
    return []

x = two_sums_optimized([3,2,4], 6)
print(x)