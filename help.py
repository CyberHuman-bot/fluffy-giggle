word = input("ENTER A WORD: ")
letter = input("ENTER A LETTER: ")
count = 0
for character in word:
    if character == letter:
        count+=1 
print(count)