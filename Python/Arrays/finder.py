# Given two arrays, find the missing element on the second one

# O(n)
def finder(array1, array2):
    set1 = set(array1)
    set2 = set(array2)

    dif = set1.difference(array2)

    return dif


# Also O(n)
def finder1(array1, array2):
    arraySet = set(array2)

    for i in array1:
        if i not in arraySet:
            return i

# With no unique elements
# O(n log n)
def finder2(array1, array2):
    array1.sort()
    array2.sort()

    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return array1[i]

# O(n)
def finder3(array1, array2):
    dic = {}
    for i in range(len(array1)):
        if array1[i] not in dic:
            dic[array1[i]] = 1
        else:
            dic[array1[i]] += 1

        if i < len(array2):
            if array2[i] not in dic:
                dic[array2[i]] = 1
            else:
                dic[array2[i]] += 1

    minel = 99999999999
    min_key = 0
    for key, value in dic.items():
        if value < minel:
            minel = value
            min_key = key
    return min_key


array1 = [1, 2, 3, 4, 5, 6, 7]
array2 = [3, 7, 2, 1, 4, 6]

print(finder(array1, array2))
print(finder1(array1, array2))
print(finder2(array1, array2))
print(finder3(array1, array2))