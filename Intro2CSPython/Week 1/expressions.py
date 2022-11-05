import math

# 1. Basic Calulator
def calc_math_expression(num1, num2, operator):
    if operator == "+" :
        return((num1) + (num2))
    elif operator == "-" :
        return ((num1)-(num2))
    elif operator == "*" :
        return((num1)*(num2))
    elif operator == ":" :
        if(num2 != 0):
            return((num1)/(num2))
    else: return(None)

# 2. extract input from string input
def calc_math_expression_from_str(str_input):
   input = str_input.split()
   num1 = float(input[0])
   num2 = float(input[2])
   operator = input[1]
   result = calc_math_expression(num1, num2, operator)
   return result


#3. Find biggest and smallest number
def find_largest_and_smallest_numbers(num1=0.0, num2=0.0, num3=0.0):
    input = [num1, num2, num3]
    input.sort()
    largest = input[2]
    smallest = input[0]
    return(largest,smallest)

#4. Quadratic equation solver
def quadratic_equation_solver(a, b, c):
    d = (b**2-4*a*c)
    if a > 0:
        if d < 0:
            return(None, None)
        elif d == 0 :
            x = (-b + math.sqrt(d)) / (2 * a)
            return(x, None)
        else :
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            return(x1, x2)

#5. Min Temp Checker
def temp_checker(min_temp, temp_1, temp_2, temp_3):
    list = [temp_1, temp_2, temp_3]
    list.sort()
    count = 0
    for i in list:
        if (i > min_temp):
            count = count+1;

    if(count >= 2):
        return(True)
    else:
        return(False)