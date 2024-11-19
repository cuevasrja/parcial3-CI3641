from sympy import binomial, floor, log, tribonacci
import sys
import time

sys.set_int_max_str_digits(1000000)

# Medimos el tiempo de ejecución
start_time = time.time()
n = int(sys.argv[1])
k = floor(log(n,2))

Narayana = binomial(n, k) * binomial(n, k - 1) / n

tribonacci_index=floor(log(binomial(n, k) * binomial(n, k - 1) / n, 2))

res = tribonacci(tribonacci_index + 1) + tribonacci(tribonacci_index)
print("--- %s seconds ---" % (time.time() - start_time))
print(res)
