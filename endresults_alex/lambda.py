def makeListSquared():
    squareRoot = lambda list : [number ** 2 for number in list]
    numbers = [1, 2, 3, 4, 5]
    print(squareRoot(numbers))

def makeListEven():
    evenNumbers = lambda list : [number for number in list if number % 2 == 0]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(evenNumbers(numbers))

makeListSquared()
makeListEven()