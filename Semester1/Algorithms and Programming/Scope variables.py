a = 100

def f():
    """
    Docstring here
    Input: a
    Output: a after being mutated
    """
    global a
    a = 300
    print(a)
f()
print(a)
print(f.__doc__)
