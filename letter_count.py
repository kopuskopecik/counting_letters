# Letter counts
sentence = input("Enter a sentence please: ")
character_dict = {}
distict_characters = set(sentence)
for letter in distict_characters:
    character_dict[letter] = sentence.count(letter)

print(character_dict)