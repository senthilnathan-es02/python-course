def vowels_count(word):
    vowels = "aeiouAEIOU"
    count =0
    for char in word:
        if char in vowels:
            count+=1
    print(count)
vowels_count("python learning")