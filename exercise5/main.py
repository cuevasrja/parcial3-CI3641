from sympy import binomial, floor, log, tribonacci
import sys
import time

sys.set_int_max_str_digits(1000000)

def maldad(n):
    """
    ### Description
    Calculate the maldad of a number n.

    ### Parameters
    - n: int - The number to calculate the maldad.

    ### Returns
    - int - The maldad of the number n.
    """
    # Calculate the Narayana number
    k = floor(log(n,2))
    Narayana = binomial(n, k) * binomial(n, k - 1) / n
    # Calculate the tribonacci number
    tribonacci_index=floor(log(Narayana, 2))
    # Calculate the maldad
    res = tribonacci(tribonacci_index + 1) + tribonacci(tribonacci_index)
    return res  

def main():
    # Get the number from the command line
    n: int
    if sys.argv[1] == "-p":
        i = 0
        n = 0
        dt = 0
        while dt <= 1:
            i += 1
            n = 2**(i)
            print("\033[1;92mNumber: ", n, "\033[0m")
            print("\033[1;92mIndex: ", i, "\033[0m")
            start = time.time()
            print(maldad(n))
            end = time.time()
            dt = end - start
            print("Time: ", dt)
            print()
        print(f"\033[1;93mLimit reached in\033[0m 2^{i} = {n}")
    else:
        n = int(sys.argv[2])
        print("Number: ", n)
        # Check the time and print the maldad of the number
        start = time.time()
        print(maldad(n))
        end = time.time()
        print("Time: ", end - start)

if __name__ == "__main__":
    main()