#default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                      make your functions more flexible, reduce number of arguments
#                      1. positional , 2. DEFAULt, 3. keyword, 4. arbitrary


# default arguments are set on the parameter level to make it constant all through
def netPrice(list_price, discount = 0, tax = 0.04):
    return list_price * (1-discount) * (1+tax)

#print(netPrice(400, 0, 0.04))   this works similar as to using default arguments
#print(netPrice(400))

print(netPrice(400,0.5))   # setting the values here overrites the default arguments passed on the parameters
