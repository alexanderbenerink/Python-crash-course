def collatz_print(col_nr:int):
    """Print the Collatz sequence starting from col_nr.

    Args:
        col_nr (int): The starting number of the Collatz sequence.
        
    Returns:
        None (print statements)
    """
    steps = 0
    col_nr_list = []
    col_nr_list.append(col_nr)

    while col_nr > 1:
        print(col_nr)
        if col_nr % 2 == 0:
            col_nr = col_nr // 2
        else:
            col_nr = 3 * col_nr + 1
        steps += 1
        col_nr_list.append(col_nr)
        
    print(col_nr)
    print(f"Number of steps: {steps}")
    print(f"Highest number in sequence: {max(col_nr_list)}")

print(__name__)

if __name__ == "__main__":
    collatz_print(5)
    # collatz_print(25)
    # collatz_print(531)