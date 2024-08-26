if __name__=="__main__":
    numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    square = lambda x: x ** 2
    squared = list(map(square, numbers))

    print(numbers)
    print("Squared: ")
    print(squared) 