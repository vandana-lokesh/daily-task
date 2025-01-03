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


