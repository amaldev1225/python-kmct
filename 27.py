words = input("Enter words separated by spaces: ").split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("The longest word is:", longest)
print("Length of the longest word:", len(longest))

