l = [1, 2, 3, 4]
for i in l:
    print(i)

"""
Write a function to unpack nested tuples and flatten them into a single tuple.  
    Example:  
    Input: `((1, 2), (3, 4), 5)`  
    Output: `(1, 2, 3, 4, 5)
"""
def flatten_tuple(t):
    flattened = []
    for i in t:
        if isinstance(i, tuple):
            flattened.extend(flatten_tuple(i))  # Recursively flatten any tuple
        else:
            flattened.append(i)  # Append non-tuple item
    return tuple(flattened)

input_tuple = ((1, 2), (3, 4), 5)
output_tuple = flatten_tuple(input_tuple)
print(output_tuple)  # Output: (1, 2, 3, 4, 5)


#factorial function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = 5
result = factorial(num)
print(result)  # Output: 1*2*3*4*5 == 120


#fibanocci series
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence

n = 7
print(fibonacci(n))  # Output: [0, 1, 1, 2, 3, 5, 8]
