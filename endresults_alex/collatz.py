import os

def collatz():
    currentStep = 1
    highestNumber = 0
    resultList = []

    while currentStep < 11:
        try:
            print('\n> Enter a number:')
            number = int(input())
            os.system('cls')
        except ValueError:
            print('Only integers allowed')
            break

        if (number % 2) == 0:
            number = (number / 2)
        else:
            number = (number * 3) + 1

        if number > highestNumber:
            highestNumber = number

        resultList.append(number)

        print('Final result: \n')

        if currentStep == 1:
            print('[Start: ' + str(number) + ']')
        
        for result in resultList:
            print('['+ str(result) +']')

        print('[Number of steps: ' + str(currentStep) + ']')
        print('[Highest number in sequence: ' + str(highestNumber) + ']')

        currentStep += 1

collatz()