# INPUT:
# nums: A list of integers representing the data set of numbers

# OUTPUT:
# A list of integers where each element is the product of all the numbers that come before it in the input list

def prefix_product(nums):
    result = []
    product = 1
    
    for i in nums:
        result.append(product)
        product = product * i
    
    return result

# Example 1: Empty list (edge case)
nums_5 = []
result_5 = prefix_product(nums_5)
print("Example 1 Result:", result_5)  # Expected Output: []

# Example 2: Standard test case with multiple elements
nums_1 = [2, 3, 4, 5]
result_1 = prefix_product(nums_1)
print("Example 2 Result:", result_1)  # Expected Output: [1, 2, 6, 24]