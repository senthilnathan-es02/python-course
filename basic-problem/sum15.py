def pallindrome(word):
    reverse = word[::-1]
    
    if  word == reverse:
            print("pallindrome")
    else:
            print("not a pallindrome")
            
pallindrome("sir")