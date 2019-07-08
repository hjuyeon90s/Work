import sys

def my_max( mymax ):
    max = sys.float_info.min
    
    for t in mymax :
        if max < t :
            max = t

    return max


print( my_max( [1, 2, 3] ) )


import sys

def my_min( mymin ):
    min = sys.float_info.max
    
    for t in mymin :
        if min > t :
            min = t

    return min


print( my_min( [1, 2, 3] ) )

def my_sum( mysum ):
    mysum = list( mysum )
    sum = mysum[ 0 ] + mysum [ 1 ]
    mysum = mysum[2:  ]
    for sum in mysum:
        if len( mysum ) != 0:
        sum = sum + mysum[0]
        mysum = mysum[ 1: ]

my_sum( 1, 2, 3, 4)
