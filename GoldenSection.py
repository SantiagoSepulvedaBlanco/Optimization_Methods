# =============================================================================
# PROJECT:    Golden Section
# AUTHOR:     Santiago Sepúlveda Blanco
# DATE:       April 2026
# 
# CONTEXT:    Code developed for educational/academic purposes.
# LICENSE:    MIT License
#             Copyright (c) 2026 Santiago Sepúlveda Blanco
#             Permission is hereby granted for use, copy, and modification, 
#             provided that the original author is credited.
# =============================================================================


import numpy as np

def f(x):
    return -(x**4)-(2*(x**3))-(8*(x**2))-5*x

def goldenSection(xl, xu, nIter):
    #Calculate x1 and x2
    d = ((np.sqrt(5)-1)/2)*(xu-xl)
    x1 = xl + d
    x2 = xu - d
    w = 12


    print(f"{'I':<5} {'xl':>{w}} {'f(xl)':>{w}} {'x2':>{w}} {'f(x2)':>{w}} {'x1':>{w}} {'f(x1)':>{w}} {'xu':>{w}} {'f(xu)':>{w}} {'d':>{w}}")
    for i in range(0,nIter,1):
        f_x1 = f(x1)
        f_x2 = f(x2)
        if(f_x1 > f_x2):
            print(f"{i+1:<5} {xl:>{w}.4g} {f(xl):>{w}.4g} {x2:>{w}.4g} {f_x2:>{w}.4g} {x1:>{w}.4g} {f_x1:>{w}.4g} {xu:>{w}.4g} {f(xu):>{w}.4g} {d:>{w}.4g}")
            xl = x2
            x2 = x1
            d = ((np.sqrt(5)-1)/2)*(xu-xl)
            x1 = xl + d
        elif(f_x2 > f_x1):
            print(f"{i+1:<5} {xl:>{w}.4g} {f(xl):>{w}.4g} {x2:>{w}.4g} {f_x2:>{w}.4g} {x1:>{w}.4g} {f_x1:>{w}.4g} {xu:>{w}.4g} {f(xu):>{w}.4g} {d:>{w}.4g}")
            xu = x1
            x1 = x2
            d = ((np.sqrt(5)-1)/2)*(xu-xl)
            x2 = xu - d

if __name__ == "__main__":
    xl = -2
    xu = 1
    nIter = 8
    goldenSection(xl, xu, nIter)