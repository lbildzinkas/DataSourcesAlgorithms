def check_anagram(list1, list2):
    list1.sort()
    list2.sort()

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False

    return True


def check_anagram1(list1, list2):
    dic = {}
    for i in range(len(list1)):
        if not list1[i] in dic:
            dic[list1[i]] = 1
        else:
            dic[list1[i]] += 1
        if not list2[i] in dic:
            dic[list2[i]] = 1
        else:
            dic[list2[i]] += 1
    for k in dic.values():
        if k % 2 != 0:
            return False
    return True


ana1 = "public relations"
ana2 = "crap built on lies"

ana1 = ana1.lower().replace(" ", "")
ana2 = ana2.lower().replace(" ", "")

print(check_anagram(list(ana1), list(ana2)))
print(check_anagram1(list(ana1), list(ana2)))
