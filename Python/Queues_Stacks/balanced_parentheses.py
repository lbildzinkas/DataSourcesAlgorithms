# Check if the brackets are balanced, for each open bracket it should have a closing one, to be considered balanced

from Queues_Stacks.stack import Stack


def balance_check(s):
    dic = {'}': '{', ')': '(', ']': '['}
    q = Stack()

    for i in s:
        if i in ['{', '(', '[']:
            q.push(i)
        else:
            if q.size() == 0:
                return False

            last = q.pop()

            match = dic[i]

            if last != match:
                return False
    return q.size() == 0



txt = '[]{{}}{}([{}])(){{}'

print(balance_check(txt))
