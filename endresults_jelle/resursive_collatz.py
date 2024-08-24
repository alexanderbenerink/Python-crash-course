def collatz(number: int, steps: int = 2, highest_number = 0) -> None:
    """Print the Collatz sequence starting from the input.

    Args:
        number (int): The starting number of the Collatz sequence.
        
    Returns:
        None, print statements only 
    """
    # Assign a new highest number when the current number is higher than the previous highest number
    highest_number: int = number if number > highest_number else highest_number
    if number == 1:
        print(f"Aantal Stappen: {steps - 1}")
        print(f"Hoogste Nummer: {highest_number}")

    elif number % 2 == 0:
        new_number: int = int(number / 2)
        print(f"[{steps}] | {new_number}")
        
        collatz(new_number, steps + 1, highest_number)
    else:
        new_number: int = int((number * 3) + 1)
        print(f"[{steps}] | {new_number}")
            
        collatz(new_number, steps + 1, highest_number)


if __name__=="__main__":
    number: int = int(input("Enter Number: "))

    print(f"[1] | {number}")
    collatz(number)

