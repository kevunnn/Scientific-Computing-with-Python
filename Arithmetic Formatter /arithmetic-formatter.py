def arithmetic_arranger(problems, solve=False):
    first_row = ''
    second_row = ''
    third_row = ''
    fourth_row = ''
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems
    for values in problems:
        split_values = values.split()
        try:
            first = int(split_values[0])
        except:
            arranged_problems = 'Error: Numbers must only contain digits.'
            return arranged_problems
        operator = split_values[1]
        if operator not in ('+','-'):
            arranged_problems = f"Error: Operator must be '+' or '-'."
            return arranged_problems
        try:
            second = int(split_values[2])
        except:
            arranged_problems = 'Error: Numbers must only contain digits.'
            return arranged_problems
        if operator == '+':
            total = first+second
        elif operator == '-':
            total = first-second
        flen = len(str(first))
        if flen > 4:
            arranged_problems = "Error: Numbers cannot be more than four digits."
            return arranged_problems
        slen = len(str(second))
        if slen > 4:
            arranged_problems = "Error: Numbers cannot be more than four digits."
            return arranged_problems
        space = max(flen,slen) + 2
        first_row += str(first).rjust(space) + ' '*4
        second_row += (operator+(' '*(space-slen-1))+str(second)).rjust(space) + ' '*4
        third_row += ('-'*(space)) + ' '*4
        fourth_row += (str(total)).rjust(space) + ' '*4
    
    first_row = first_row.rstrip()
    second_row = second_row.rstrip()
    third_row = third_row.rstrip()
    fourth_row = fourth_row.rstrip()
    
    if solve:
        arranged_problems = '\n'.join((first_row, second_row, third_row, fourth_row))
    else:
        arranged_problems = '\n'.join((first_row, second_row, third_row))
    return arranged_problems
