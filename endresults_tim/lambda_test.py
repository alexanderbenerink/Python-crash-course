l = [1, 2, 3, 4, 5]
print(list(map(lambda x: x ** 2, l)))  # Output: [1, 4, 9, 16, 25]

# Lambda function to filter out the even numbers from a list
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x % 2 == 0, l2)))  # Output: [2, 4, 6, 8, 10]