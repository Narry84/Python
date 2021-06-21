


def Palindrome_Tester():
    # variable to store user input
    word=input(("Enter a word:"))
    #if statement - if word reads the same forward and backwards display message
    if(word==word[::-1]):
      print(word,"is a palindrome")
    #if statement - else (word does not read the same forward and backward) display below message
    else:
      print(word, "is NOT a palindrome")
    Palindrome_Tester()
#Call function
Palindrome_Tester()




