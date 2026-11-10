numbers = input("Enter numbers separated by spaces: ")

num_list = list(map(int, numbers.split()))

total = sum(num_list)

print("Sum =", total)

