# Some messages from the description
msg_0 = "Enter an equation\n"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):\n"
msg_5 = "Do you want to continue calculations? (y / n):\n"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)\n"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)\n"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)\n"
# Calculator starts with empty memory. Before any calculation result is N/D. "is_continue" is a safe word
memory = 0.0
is_continue = True


def taking_input():
    global memory

    # Collecting operands "x" and "y" and operator from input like "x + y" until it's valid
    while True:
        x, operator, y = input(msg_0).split()
        # Check if user wants to use memory variable for "x" or "y"
        if x == "M":
            x = memory
        if y == "M":
            y = memory
        # If at least one operand is a literal - raising error, restarting cycle
        try:
            float(x)
        except ValueError:
            print(msg_1)
        else:
            try:
                float(y)
            except ValueError:
                print(msg_1)
            else:
                # Validating operator
                if operator not in "+-*/":
                    print(msg_2)
                else:
                    return [x, y, operator]


def check(x, y, operator):
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg = msg + msg_6
    if (float(x) == 1 or float(y) == 1) and operator == "*":
        msg = msg + msg_7
    if (float(x) == 0 or float(y) == 0) and (operator == "*" or operator == "+" or operator == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def is_one_digit(v):
    v = str(v)
    if "." in v:  # v is float
        if -10 < float(v) < 10:  # is it more than 10?
            if has_mean_part(v):  # Is after "." there something else than 0?
               return False
            else:
                return True
        else:
            return False
    else:
        if len(v) > 1:
            return False
        else:
            return True


def has_mean_part(float_as_string):
    parts = float_as_string.split(".")  # Dividing float to parts
    more_than_zero = 0
    # If right part of float contain something more than 0 - it is not something like 5.0(0)
    for i in parts[1]:
        if i != "0":
            more_than_zero += 1
    if more_than_zero > 0:
        return True
    else:
        return False


def calc(x, y, operator):
    if operator == "/" and float(y) == 0.0:  # Checking possible DivisionByZero
        print(msg_3)
    else:
        x = float(x)
        y = float(y)
        if operator == "/":
            result = x / y
        elif operator == "+":
            result = x + y
        elif operator == "-":
            result = x - y
        else:
            result = x * y
        return result


def is_save_result(result):
    # Checking if user wants to store result in memory?
    while True:
        is_to_memory = input(msg_4)
        if is_to_memory == "y":
            if is_one_digit(result):
                msg_index = 10
                while msg_index < 13:  # Cycling during "y", break after one "n" or after msg_12
                    is_to_memory = input(globals()["msg_" + str(msg_index)])
                    if is_to_memory == "y":
                        msg_index += 1
                    elif is_to_memory == "n":
                        break
                    else:
                        continue
                if is_to_memory == "y":
                    return True
                else:
                    return False
            else:
                return True
        elif is_to_memory == "n":
            break
        else:
            pass


def is_enough():
    while True:
        is_continue = input(msg_5)
        if is_continue == "y":
            return False
        elif is_continue == "n":
            return True
        else:
            pass  # User entered something beside correct answer. Asking again


while True:
    data = taking_input()
    x = data[0]
    y = data[1]
    operator = data[2]
    check(x, y, operator)
    result = calc(x, y, operator)
    if result is None:
        continue
    else:
        print(result)
    if is_save_result(result):
        memory = result
    # Checking if user wants to calculate something else?
    if is_enough():
        break
