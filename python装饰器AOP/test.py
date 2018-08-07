
def modify(function):
    print"modify"
    return function

@modify
def fun():
    print"this is the fun()"

fun()