def vowels(letter):
    vowel = "aeiouAEIOU"
    count= 0
    for letter in letter:
        if letter in vowel:
            count+=1

    print(count)
vowels("senthilnathan")