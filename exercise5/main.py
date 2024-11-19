from sympy import binomial, floor, log, tribonacci
import sys
import time

sys.set_int_max_str_digits(1000000)

def maldad(n):
    k = floor(log(n,2))
    Narayana = binomial(n, k) * binomial(n, k - 1) / n
    tribonacci_index=floor(log(Narayana, 2))
    res = tribonacci(tribonacci_index + 1) + tribonacci(tribonacci_index)
    return res  

def main():
    n = int(sys.argv[1])
    start = time.time()
    print(maldad(n))
    end = time.time()
    print("Time: ", end - start)

if __name__ == "__main__":
    main()