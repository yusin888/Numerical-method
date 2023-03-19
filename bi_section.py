import math
import timeit


def f(x):
   return x**3-2*x-5

    # return x**3

a=2
b=3
tolerance= 1e-6
max_iteration=100

for i in range(max_iteration):

    c=(a+b)/2
#    print(c)

    if abs(f(c)) < tolerance:
        print(f"Root found at x={c:.6f}")
        print("The time taken is ",timeit.timeit())

        break
    

    elif f(c)*f(a) <0 :
        b=c
    else:
        a=c


