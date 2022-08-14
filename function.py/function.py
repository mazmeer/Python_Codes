def main_fun(a, b):
    
    def addition(a, b):
        return a + b

    # function ka locha
    add = addition(a, b)
    # add 5 to the result
    return add + 5


result = main_fun(3, 5)
print(result)
