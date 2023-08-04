'''
def reverse_string(string):
    reversed_string = ''
    index = len(string) - 1

    while index >= 0:
        reversed_string += string[index]
        index -= 1

    return reversed_string

# Example usage
input_string = "Hello, World!"

reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)

'''


'''
def is_palindrome(string):
    # Remove whitespaces and convert to lowercase
    string = string.replace(" ", "").lower()
    length = len(string)
    is_palindrome = True

    for i in range(length // 2):
        if string[i] != string[length - i - 1]:
            is_palindrome = False
            break

    return is_palindrome

# Example usage
input_string = "Able was I saw eLba"

if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")



def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base, -exponent)
    else:
        return base * power(base, exponent - 1)

# Example usage
base = 2
exponent = 3

result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
number = 5

result = factorial(number)
print(f"The factorial of {number} is: {result}")
