for x in range(1,100):
    if (int(x) % 3 == 0) and (int(x) % 5 == 0):
        print ("fizzbuzz")
    elif (int(x) % 3 == 0):
        print ("fizz")
    elif (int(x) % 5 == 0):
        print ("buzz")
    else:
        print (x)
    