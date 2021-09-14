def mysum(*args):
    output = 0
    for y in args:
        output += y
    return output
print(mysum(2, 4, 8))

"""
in the above function, the splat operator is used to get the sum of the 
integers after the iteration, henceforth the function mysum(), is called.  

the above function can be compared with the one below, where built in function sum()
does the same thing.
"""

def dd():
    dd = [2, 4, 8]
    print(sum(dd))
dd()


name = 'emmanuel mkpurunchi f'
title = 'mysum function assignment'
print(f'Name: {name.upper()}. \n Title: {title.upper()}. \n')

