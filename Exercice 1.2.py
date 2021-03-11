import random   #import

x = (random.randint(0,100)) # define x

print(x)  # show x for test
a = int(input('guess a number between 0 and 100: ')) # guess

while a < x:    # to small
    print ('your value is to small')
    a = int(input('guess a new number between 0 and 100: '))
    while a > x:   # to large
        print('your value is to large')
        a = int(input('guess a new number between 0 and 100: '))
else:    # bravo
        print('bravo')

#TEST







