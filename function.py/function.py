def main_fun(a, b):
    
    def addition(a, b):
        return a + b

    # call inner function from outer function
    add = addition(a, b)
    # add 5 to the result
    return add + 5

result = main_fun(4, 5)
print(result)
