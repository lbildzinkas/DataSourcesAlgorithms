# given an array and a number, find all possible pair sums in the array that results the number

# O(n square)
def pair_sum(list, number):
    count = {}

    for i in list:
        for k in list:
            if i + k == number:
                formatted_pair = format_pair(i, k)
                if formatted_pair not in count:
                    count[formatted_pair] = 1
    return count.keys()


def format_pair(i, k):
    if i >= k:
        return '({0},{1})'.format(k, i)
    else:
        return '({0},{1})'.format(i, k)


# O(n)
def pair_sum1(list, number):
    result = set()
    memory = set()

    for i in list:
        target = number - i
        if target not in memory:
            memory.add(i)
        else:
            result.add((min(i, target), max(i, target)))
    return result


list = {1, 2, 7, 3, 2, 10, 19, 4, 8, 1, 6}
number = 6

count = pair_sum(list, number)
count1 = pair_sum1(list, number)

print(len(count))
print(len(count1))

# print('/n'.join(map(str, list(count))))
# print('/n'.join(map(str, list(count1))))
