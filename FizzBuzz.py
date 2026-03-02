def FizzBuzz(start, finish):
    outlist = []
    for n in range(start, finish + 1):
        if n % 15 == 0:
            outlist.append("fizzbuzz")
        elif n % 3 == 0:
            outlist.append("fizz")
        elif n % 5 == 0:
            outlist.append("buzz")
        else:
            outlist.append(n)
    return(outlist)
