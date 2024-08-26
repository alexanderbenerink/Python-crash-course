def lambda_squared(numbers: list) -> list:
    square = lambda x: x ** 2
    squared = list(map(square, numbers))

    return squared

def lambda_even(numbers: list) -> list:
    even = lambda x: x % 2 == 0
    even_list = list(filter(even, numbers))

    return even_list

if __name__=="__main__":
    numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    print(numbers)
    print('Squared: ')
    print(lambda_squared(numbers))

    print('\n')
    
    print(numbers)
    print('Even: ')
    print(lambda_even(numbers))

