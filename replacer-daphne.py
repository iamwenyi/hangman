def replace(word,alphabet_change,alphabet_replace):
    for x in range(0,len(word)):
        if word[x] == alphabet_change:
            word = word[0:x] + alphabet_replace + word[x+1:len(word)]
    return word

word = input("Enter a word: ")
alphabet_change = input("Enter the alphabet you want to change: ")
alphabet_replace = input("Enter the alphabet you want to replace it with: ")

word = replace(word,alphabet_change,alphabet_replace)
print(word)
