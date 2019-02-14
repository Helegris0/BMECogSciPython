import sys

numbers = []
for arg in sys.argv[1:]:
  numbers.append(int(arg))

ari_mean = sum(numbers) / len(numbers)
print('Arithmetic mean: ' + str(ari_mean))

def get_geometric_mean(nums):
    product = 1
    for number in numbers:
        product = product * number
    return product ** (1/len(numbers))

print('Geometric mean: ' + str(get_geometric_mean(numbers)))

def get_smallest(nums):
    smallest = nums[0]
    for number in nums:
        if (number < smallest):
            smallest = number
    return smallest

def get_greatest_common_divisor(nums):
    smallest = get_smallest(nums)
    result = 1

    for i in range(smallest, 0, -1):
        is_common = True
        for j in nums:
            if (j % i != 0):
                is_common = False
        if (is_common):
            return i

print('Greatest common divisor: ' + str(get_greatest_common_divisor(numbers)))
