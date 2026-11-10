str1 = input("Enter a string: ")

freq = {}

for i in str1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Character frequency:")

for key, value in freq.items():
    print(key, ":", value)

