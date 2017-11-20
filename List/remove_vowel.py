vowels='aeiou'
sentence=[]
sentence=str(input())
new_sentence=[]
for letter in sentence:
    if letter not in vowels:
        new_sentence.append(letter)
print(''.join(new_sentence))
