# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def take_input():
    print('This is a quadratic equation root finder please specify the coefficients with regards to equation: y = ax^2 + bx +c')
    print('Input a:')
    a = input()
    print('Input b:')
    b = input()
    print('Input c:')
    c = input()
    out = [float(a), float(b), float(c)]
    return out

def calc_roots(coeff_list):
    delta = coeff_list[1]**2 -4*coeff_list[0]*coeff_list[2]
    if delta > 0:
        x1 = (-coeff_list[1]+math.sqrt(delta))/(2*coeff_list[0])
        x2 = (-coeff_list[1]-math.sqrt(delta))/(2*coeff_list[0])
        return x1, x2

    elif delta == 0:
        x0 = -coeff_list[1]/(2*coeff_list[0])
        return x0



if __name__ == '__main__':
    coeff_list = take_input()
    out = calc_roots(coeff_list)
    print('Calculated roots are:')
    print(out)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
