def arithmetic_arranger(problems, display = False):

    arranged_problems = ""

    dividends = [dividend.split(" ")[0] for dividend in problems]
    operators = [operator.split(" ")[1] for operator in problems]
    divisors = [divisor.split(" ")[2] for divisor in problems]
    paddings = [max(len(dividends), len(divisors)) for dividends, divisors in zip(dividends, divisors)]
   
    if len(problems) > 5:
        arranged_problems = f"Error: Too many problems."
    if not all(operator in ["+","-"] for operator in operators):
        arranged_problems = f"Error: Operator must be '+' or '-'."
    if not all((dividend.isdigit() and divisor.isdigit()) for dividend, divisor in zip(dividends, divisors)):
        arranged_problems = f"Error: Numbers must only contain digits."
    if not all((len(dividend) <= 4 and len(divisor) <= 4) for dividend, divisor in zip(dividends, divisors)):
        arranged_problems = f"Error: Numbers cannot be more than four digits."
    
    if len(arranged_problems) == 0:

        arranged_problems += "    ".join([(f"  {dividend:>{pad}}") for dividend, pad in zip(dividends, paddings) ]) + "\n"

        arranged_problems += "    ".join([(f"{operator} {divisor:>{pad}}") for operator, divisor, pad in zip(operators, divisors, paddings)]) + "\n"

        arranged_problems += "    ".join([(f"{'-'*(pad+2)}") for pad in paddings])

        if display:

            arranged_problems += "\n" + "    ".join([f"{int(dividend) + int(divisor):>{pad+2}}" if operator == "+" else f"{int(dividend) - int(divisor):>{pad+2}}" for dividend, operator, divisor, pad in zip(dividends, operators, divisors, paddings)])
    
    return arranged_problems


number_of_problems = 0

problems = []
problem = ""
display_answer = ""

run = True
while run:

    while run:
        try:
            first_number = int(input("Enter first number (0 - 9999): ")) 
            if 0 <= first_number <= 9999:
                problem += str(first_number) + " "
                break
        except ValueError:
            print("Enter only between (0 - 9999)!")

    while run:
        try:
            operator = input("Choose operator ('+' or '-'): ")
            if operator == '+' or operator == '-':
                problem += operator + " "
                break
        except TypeError:
            print("Choose only between addition or subtraction!")

    while run:
        try:
            second_number = int(input("Enter second number (0 - 9999): "))
            if 0 <= second_number <= 9999:
                problem += str(second_number)
                break
        except ValueError:
            print("Enter only between (0 - 9999)!")
    
    print()
    problems.append(problem)
    number_of_problems += 1
    print(f"You have entered {number_of_problems}/5 problems.")
    print()

    while run:
        try:
            new_problem = input("Do you want to add new problem?(Y or N): ")
            if new_problem == "Y" or new_problem == "y":
                break
            if new_problem == "N" or new_problem == "n":

                while run:
                    try:
                        answer = input("Display the answer? ('Y' or 'N'): ")
                        if answer == 'Y' or answer == 'y':
                            display_answer = True
                        if answer == 'N' or answer == 'n':
                            display_answer = False

                        if display_answer or not display_answer:
                            print()
                            print(arithmetic_arranger(problems, display_answer))
                            run = False
                            break
                    except TypeError:
                        print("Enter only 'Y' or 'N'")
                

        except TypeError:
            print("Enter only correct letter!")

    print()
    