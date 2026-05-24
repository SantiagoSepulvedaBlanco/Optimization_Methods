import numpy as np

def function(x, y):
    f = 4*(np.e**(0.8*x)) - (0.5)*y
    return f

def HuntMethod(xi, xf, yi, h, n_iters):

    results = []

    for x_i in range(int(np.abs(xi - xf))):
        #Aplicamos metodo de hunt
        print("\n\nHunt Method for x= " , x_i + 1)
        f_xi_yi = function(x_i, yi)
        yi_1 = yi + (f_xi_yi*h)
        print("solution without correction: ", yi_1)
        #Aplicamos la correcion
        print("Solutions with corrections: ")
        for i in range(n_iters):
            yi_1 = yi + ((f_xi_yi + function(x_i+h, yi_1))/2)*h
            if i == 0:
                print("Iter #", i + 1," result = ", yi_1)
            elif n_iters > 1:
                if n_iters == i+1:
                    print("Iter #", i + 1," result = ", yi_1)
        yi = yi_1

def runCode():
    print("PLEASE ENTER THE VALUES FOR THE RESPECTIVE FUNCTION: ")
    xi = float(input("Please enter the initial x value: "))
    xf = float(input("Please enter the final x value: "))
    yi = float(input("Please enter the correct y image for x initial value: "))
    h = float(input("Please enter the step size: "))
    n_iters = int(input("Please enter the number of corrections for each value to evaluate: "))
    HuntMethod(xi, xf, yi, h, n_iters)

runCode()