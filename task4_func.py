# function examples

# example 1 -

def add_numbers(num1, num2):
    print(f'num1 = {num1}')
    print(f'num2 = {num2}')
    return num1 + num2

result = add_numbers(5, 10)

print(f'Result of addition: {result}')


# example 2 -

def max_num(a, b, c):
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
    return max(a, b, c)
 
result = max_num(-3, 7, 5)

print(f'max num is : {result}') 

