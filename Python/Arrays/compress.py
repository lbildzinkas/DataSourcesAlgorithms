# Given an string, compress it in a way that "AAABBCC" turns into "A3B2C2"

# O(n)
def compress(txt):
    current_letter_counter = 0
    current_letter = txt[0]
    result = ''

    for i in range(len(txt)):
        if txt[i] != current_letter:
            result = result + current_letter + str(current_letter_counter)
            current_letter = txt[i]
            current_letter_counter = 0

        current_letter_counter += 1

        if i == len(txt) - 1:
            result = result + current_letter + str(current_letter_counter)

    return result


txt = "AAABBCCaaDDeffFGPPPpOm"

print(compress(txt))
