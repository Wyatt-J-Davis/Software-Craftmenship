def fizzbuzz_calculate(i):
    fizz = True if i%3 == 0 else False # Determine whether value should be replaced by "fizz"
    buzz = True if i%5 == 0 else False # Determine whether value should be replaced by "buzz"
   
    if(fizz and buzz): # If both fizz and buzz booleans are true print "fizzbuzz"
        return "fizzbuzz"
    elif(fizz): # If just fizz boolean is true then print "fizz"
        return "fizz"
    elif(buzz): # If just buzz boolean is true then print "buzz"
        return "buzz"
    else:
       return i # Print the iterator value, i, if neither fizz nor buzz is true