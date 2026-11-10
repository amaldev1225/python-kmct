s = input("Enter a string: ")

if len(s) >= 2:
    s = s[-1] + s[1:-1] + s[0]

print("String after exchanging first and last characters:", s)

