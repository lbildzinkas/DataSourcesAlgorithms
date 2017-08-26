# Given an string, check if all the elements of the string are unique

# O(n)
def is_unique(txt):
    check_set = set()
    for i in txt:
        if i in check_set:
            return False
        else:
            check_set.add(i)
    return True


txt = "abcdefghtt"

print(is_unique(txt))
