#INPUT:
# start, the integer describing the Celsius degree we are starting our conversions from
# stop, the last integer we want to include for doing our conversions. We should also return its Fahrenheit conversion

# OUTPUT:
# Print every fahrenheit conversion between start and stop inclusive as a float
# Return the fahrenheit conversion of stop
def temp_conversion(start, stop):
    for temp in range(start,stop+1):
        conversion = ((9/5) * temp) + 32
        print(round(conversion,2))
    return conversion

print(temp_conversion(0, 5))


# Should output:
# 
#  32.0
#  33.8
#  35.6
#  37.4
#  39.2
#  41.0
#  41.0 --> outputs 41.0 twice because it is the return value