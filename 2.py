numbers = [-5, 3, -2, 8, 0, 6, -1]
positive = [x for x in numbers if x > 0]
print(positive)


n = int(input("Enter N: "))
squares = [x * x for x in range(1, n + 1)]
print(squares)

word = input("Enter a word: ")
vowels = [ch for ch in word if ch in 'aeiouAEIOU']
print(vowels)

word = input("Enter a word: ")
ordinal_values = [ord(ch) for ch in word]
print(ordinal_values)

