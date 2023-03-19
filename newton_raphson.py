import timeit
def f(x):
    return x**3 - 2*x -5
def df(x):
    return 3*x**2 -2
x0 = 1
tolerance = 1e-6
maxiterr = 100
for i in range(maxiterr):
    fx = f(x0)
    dfx = df(x0)
    
    x1 = x0 - (fx/dfx)
    
    if abs(f(x1)) < tolerance:
        print(f"Root found at x = {x1:.6f}")
        print("The time taken is ",timeit.timeit())
        break
    else:
        x0 = x1