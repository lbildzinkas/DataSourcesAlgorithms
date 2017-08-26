# Reverse the words of a given string

# O(n)
def sentence_reversal(txt):
    txt = txt.strip()
    result = ""
    lastWordStart = len(txt)
    index = -1

    for i in reversed(txt):
        if i == ' ' or index == -(len(txt)):
            result += txt[index: lastWordStart] + " "
            lastWordStart = index
        index -= 1

    return result


txt = "This is the best"

print(sentence_reversal(txt))
