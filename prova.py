import __main__, os
print(__main__.__file__)

f = open(__main__.__file__, 'r')
print(f.readlines())