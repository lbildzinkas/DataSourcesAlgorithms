# Given an array, calculate the largest possible continuous sum

# not saving the elements
# O(n)
def largest_continuous_sum(list):
    largest_sum = 0
    last_largest_sum = 0
    continuous_sum = 0

    for i in list:
        if last_largest_sum > continuous_sum and last_largest_sum > largest_sum:
            largest_sum = last_largest_sum

        last_largest_sum = continuous_sum
        continuous_sum += i

        if continuous_sum > largest_sum:
            largest_sum = continuous_sum

    return largest_sum


# Tracking the elements of the sum
# O(n)
def largest_continuous_sum1(list):
    max_sum = (-1, [])
    last_largest_sum = 0
    continuous_sum = 0

    for i in range(len(list)):
        if last_largest_sum > continuous_sum and last_largest_sum > max_sum[0]:
            max_sum = (last_largest_sum, list[:i+1])

        last_largest_sum = continuous_sum
        continuous_sum += list[i]

        if continuous_sum > max_sum[0]:
            max_sum = (continuous_sum, list[:i+1])
    return max_sum


list = [1, 2, -1, 3, 4, 10, 10, -10, -1]
list1 = [1, 2, -1, 3, 4, -1]
list2 = [1, 2, -1, 3, 4, -1, -20, -30, -70, 200, 500]

print(largest_continuous_sum1(list2))
