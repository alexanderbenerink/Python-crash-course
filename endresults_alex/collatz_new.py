def collatz(number:int):
    steps = 0
    sequence = []

    while number > 1:
        
        if steps == 0:
            print(f"[Start: {int(number)}]")

        if (number % 2) == 0:
            number = (number / 2)
        else:
            number = (number * 3) + 1
        
        steps += 1
        sequence.append(number)

        print(f"[{int(number)}]")

    print(f"[Number of steps: {int(steps)}]")
    print(f"[Highest number in sequence: {int(max(sequence))}]")

collatz(531)