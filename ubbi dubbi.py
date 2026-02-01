def ubbi_dubbi_word(word):
    word = word.lower()
    eword = ""
    length = len(word)
    i = 0
    while i != length:
        if i == length - 1:
            if word[i] == "e":
                eword += word[i]
        elif word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u" or word[i] == "y":
            eword += "ub"
            eword += word[i]
        else:
            eword += word[i]
        i += 1
    return eword


def ubbi_dubbi_sentence(sentence):
    sentence = sentence.lower()
    esentence = ""
    sentence = sentence.split()
    for word in sentence:
        esentence += ubbi_dubbi_word(word) + " "
    return esentence



print(ubbi_dubbi_word("hello"))
print(ubbi_dubbi_sentence("look! his tie is ugly."))

w = "ubbi dubbi"
for i in range(1, 6):
    w = ubbi_dubbi_word(w)
    print(i, w)