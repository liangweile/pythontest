

def modify(function):
    print "1"
    return function
@modify
def func():
    print "function"

func();