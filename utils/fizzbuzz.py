def fizzbuzz_calculate(i):
    fizz = True if i%3 == 0 else False # Determine whether value should be replaced by "fizz"
    buzz = True if i%5 == 0 else False # Determine whether value should be replaced by "buzz"
   
    if(fizz and buzz): # If both fizz and buzz booleans are true print "fizzbuzz"
        print("fizzbuzz")
    elif(fizz): # If just fizz boolean is true then print "fizz"
        print("fizz")
    elif(buzz): # If just buzz boolean is true then print "buzz"
        print("buzz")
    else:
       print(i) # Print the iterator value, i, if neither fizz nor buzz is true