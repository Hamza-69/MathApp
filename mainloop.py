import importlib


functions = {
        "Define functions in form":"FunctionName(variable) = expression",
        "pi()":"value of pi()",
        "cos(x)":"Return the cosine after the expression is evaluated",
        "sin(x)":"Return the sine after the expression is evaluated",
        "tan(x)":"Return the tangent after the expression is evaluated",
        "cot(x)":"Return the cotangent after the expression is evaluated",
        "sec(x)":"Return the secant after the expression is evaluated",
        "csc(x)":"Return the cosecant after the expression is evaluated",
        "arccos(x)":"Return the arccosine after the expression is evaluated",
        "arcsin(x)":"Return the arcsine after the expression is evaluated",
        "arctan(x)":"Return the arctangent after the expression is evaluated",
        "arccot(x)":"Return the arccotangent after the expression is evaluated",
        "arcsec(x)":"Return the arcsecant after the expression is evaluated",
        "arccsc(x)":"Return the arccosecant after the expression is evaluated",
        "cosh(x)":"Return the hyperbolic cosine after the expression is evaluated",
        "sinh(x)": "Return the hyperbolic sine after the expression is evaluated",
        "tanh(x)": "Return the hyperbolic tangent after the expression is evaluated",
        "coth(x)": "Return the hyperbolic cotangent after the expression is evaluated",
        "sech(x)": "Return the hyperbolic secant after the expression is evaluated",
        "csch(x)": "Return the hyperbolic cosecant after the expression is evaluated",
        "arcosh(x)": "Return the hyperbolic arcosine after the expression is evaluated",
        "arsinh(x)": "Return the hyperbolic arsine after the expression is evaluated",
        "artanh(x)": "Return the hyperbolic artangent after the expression is evaluated",
        "arcoth(x)": "Return the hyperbolic arcotangent after the expression is evaluated",
        "arsech(x)": "Return the hyperbolic arsecant after the expression is evaluated",
        "arcsch(x)": "Return the hyperbolic arcosecant after the expression is evaluated",
        "exp(x)":"Return the exponential after the expression is evaluated",
        "exp_base(x,b)":"Return the exponential base b after the expression is evaluated",
        "log(x,b)":"Return the logarithm after the expression is evaluated",
        "ln(x)":"Return the natural logarithm after the expression is evaluated",
        "nth_root(x,n)":"Return the nth_root after the expression is evaluated",
        "sqrt(x)":"Return the square root after the expression is evaluated",
        "abs(x)":"Return the absolute value after the expression is evaluated",
        "factorial(x)":"Return the factorial after the expression is evaluated",
        "combination(n,r)":"Return the combination of n & r",
        "permutation(n,r)":"Return the permutation of n & r"
    }


def removeAll(string, removed):
    while removed in string:
        string = string.replace(removed, '')
    return string


def take_function(function_string):
    if "=" not in function_string:
        print("Invalid input! Please enter the function in the format 'function_name=expression'.")
        return "0", "1"

    function = removeAll(function_string, " ").split("=")
    if len(function) != 2:
        print("Invalid input! Make sure the function name is valid and the input is correct.")
        return "0", "1"

    function_name = function[0]
    function_body = function[1]
    if function_name in functions:
        print("Invalid input! Function name is already taken.")
        return "0", "1"

    function_code = f"def {function_name}:\n    return {function_body}\n\n"

    try:
        with open("functions_list.py", "a") as f:
            f.write(function_code)
        print(f"Function '{function_name}' added")
        import functions_list
        importlib.reload(functions_list)
        return function
    except:
        print("Invalid input! Make sure the function name is valid and the input is correct.")
        return "0", "1"

def substitute_function(function_call):
    try:
        with open("function_calls.py", "a") as f:
            f.write(f"print({function_call})\n")
        import function_calls
        importlib.reload(function_calls)
    except:
        print("Invalid input! Make sure the function name is valid and has been defined.")
    with open("function_calls.py", "w") as f:
        f.write(f"from functions_list import *\n")

def main():
    while True:
        action = input("Enter function to define, or expression to evaluate (q to quit/ h for help): ")
        action = removeAll(action, " ")
        if action == "q":
            break
        elif action == "h":
            print(f"{'_'*18} Welcome to MathApp 1.0!! {'_'*18}\n")
            for i,j in functions.items():
                print(f"{i}: {j}")
            print("")
        elif "=" in action and action[0].isalpha() and action[1] == "(" and action[2].isalpha():
            function = take_function(action)
            if function[0] == "0":
                continue
            functions[function[0]] = f'Return {function[1]}'
        else:
            substitute_function(action)
    with open("functions_list.py", "w") as f:
        f.write("")
        f.close()


if __name__ == '__main__':
    main()
