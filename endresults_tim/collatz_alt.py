def collatz(number, step=0, max=0):
    remainder = number % 2
    if remainder == 0: # even
        number = int(number / 2)
    else: # oneven
        number = number * 3 + 1
    step = step + 1 # count the step
    if number > max: # check for max
        max = number
    print(number, "(step={}, max={})".format(step, max) )
    if number > 1:
        collatz(number,step, max)

collatz(11)