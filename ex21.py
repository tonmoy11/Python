def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" %(a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "I will some math with just function!"

age = add(30, 5)
height = subtract (98, 2)
weight = multiply (90,2)
iq = divide( 100, 2)

print "Age: %d , Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

#puzzle to do
print "Here is the puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print "That becomes: ", what, "Lets do it by hand?"

##################
# def x(arg):
#     print "scheck %s" % argv
#     return a
#
# c = x(30)
# print "its retunrung %r" % c
